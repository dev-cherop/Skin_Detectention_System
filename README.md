# Skin Cancer Detection Django Project

**Author:** devcherop  


---

## Project Overview
The **Skin Cancer Detection Django Project** is a web application that allows users to detect skin cancer from images using machine learning models. The project leverages a combination of **Naive Bayes** and **SVM** models to provide predictions for different types of skin lesions.

---

## Features
- Upload images of skin lesions for detection.
- Prediction using pre-trained machine learning models:
  - `naive_bayes.pkl`
  - `svm.pkl`
- User-friendly interface built with Django.
- Static assets managed under `static/img`.
- Core functionality encapsulated in the `coreapp`.

---

## Installation

1. **Clone the repository:**
git clone https://github.com/dev-cherop/Skin_Detectention_System.git

cd Skin_Detectention_System
Create a virtual environment and activate it:


python -m venv venv

source venv/bin/activate     # Linux/Mac

venv\Scripts\activate       # Windows
Install dependencies:

pip install -r requirements.txt
Run migrations:


python manage.py migrate
Start the development server:


python manage.py runserver
Access the app:
Open http://127.0.0.1:8000 in your browser.

Usage
1.Navigate to the upload page.

2.Upload an image of the skin lesion.

3.The system will return a prediction using the trained models.

4.Interpret results carefully and consult a healthcare professional for medical advice.

