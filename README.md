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

## Project Structure
SkinDetectorProject/
│
├── coreapp/ # Main Django app containing models, views, and templates
├── static/img/ # Static images used in the project
├── naive_bayes.pkl # Pre-trained Naive Bayes model
├── svm.pkl # Pre-trained SVM model
├── manage.py # Django management script
├── .gitignore # Git ignore rules
└── README.md # Project documentation

yaml
Copy code

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/dev-cherop/Skin_Detectention_System.git
cd Skin_Detectention_System
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the app:
Open http://127.0.0.1:8000 in your browser.

Usage
Navigate to the upload page.

Upload an image of the skin lesion.

The system will return a prediction using the trained models.

Interpret results carefully and consult a healthcare professional for medical advice.

