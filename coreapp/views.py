from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
import shutil
import os
import easygui
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from coreapp import predict
import pandas  as pd


def base(request):
    return render(request, 'coreapp/home.html')


@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, 'coreapp/signup.html')

    elif request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpass = request.POST.get('cpass')

        if password != cpass:
            easygui.msgbox("The two passwords do not match", title="Error")
            return redirect('base')

        # save user to CSV
        with open(os.path.join(os.path.dirname(__file__), 'database.csv'), 'a') as file:
            file.write(f"{fullname},{email},{password}\n")

        easygui.msgbox("Successfully registered", title="Success")
        return redirect('login')

    # fallback
    return render(request, 'coreapp/signup.html')


@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, 'coreapp/login.html')

    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        flag = False
        with open(os.path.join(os.path.dirname(__file__), 'database.csv'), 'r') as file:
            for line in file:
                line = line.strip().split(",")
                if line[1] == email and line[2] == password:
                    with open(os.path.join(os.path.dirname(__file__), "session.txt"), "w+") as f:
                        f.write(line[0])
                    flag = True
                    break

        if flag:
            with open(os.path.join(os.path.dirname(__file__), "session.txt"), "r") as f:
                name = f.read()
            return render(request, 'coreapp/index.html', {"name": name})
        else:
            easygui.msgbox("Incorrect Username or password", title="Error")
            return redirect('login')

    return render(request, 'coreapp/login.html')


@csrf_exempt
def logout(request):
    return redirect('base')


@csrf_exempt
def dashboard(request):
    with open(os.path.join(os.path.dirname(__file__), "session.txt"), "r") as f:
        name = f.read()
    return render(request, 'coreapp/index.html', {"name": name})


@csrf_exempt
def submit(request):
    if request.method == "POST":
        image = request.FILES['image']

        img_dir = os.path.join(os.getcwd(), 'static', 'img')
        if os.path.exists(img_dir):
            shutil.rmtree(img_dir)
        os.makedirs(img_dir, exist_ok=True)

        path = default_storage.save(os.path.join(img_dir, 'result.jpg'), ContentFile(image.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        result = predict.process()
        result = result.split('/')

        with open(os.path.join(os.path.dirname(__file__), "session.txt"), "r") as f:
            name = f.read()

        return render(request, 'coreapp/result.html', {
            "result": result[0],
            "name": name,
            "description": result[1]
        })

    return redirect('dashboard')