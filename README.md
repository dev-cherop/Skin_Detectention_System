# Skin Cancer Detection Django Project

**Author:** devcherop  
**Initial Commit:** 5 days ago  

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
```bash
2. git clone https://github.com/dev-cherop/Skin_Detectention_System.git
cd Skin_Detectention_System

3. python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

4. pip install -r requirements.txt

5. python manage.py migrate

6. python manage.py runserver
 
