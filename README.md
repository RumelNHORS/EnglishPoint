# EnglishPoint

**EnglishPoint** is a comprehensive online and offline platform for English learning, IELTS preparation, and visa processing services. This project is built using Django and Django Rest Framework to manage its backend functionalities.

---

## Features

### 1. **Online and Offline English Learning**
- General English
- Spoken English
- Business English

### 2. **IELTS Preparation**
- Comprehensive preparation for all four sections (Listening, Reading, Writing, Speaking)
- Tips and strategies to maximize band scores

### 3. **Visa Processing Services**
- Student visa support
- Work and immigration visa consultancy
- End-to-end guidance, including documentation and eligibility checks

---

## Technology Stack
- **Backend Framework:** Django 5.1
- **API:** Django Rest Framework (DRF)
- **Database:** MySQL (PySQL integration)
- **Frontend:** To be connected with React.js or templates (if applicable)
- **Deployment:** Compatible with cPanel hosting or cloud servers

---

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- MySQL server
- Virtual environment (optional but recommended)

### Steps
1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd EnglishPoint
Set Up the Environment

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure the Database

Create a MySQL database.
Update the DATABASES section in englishpoint/settings.py with your MySQL credentials.
Run Migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser

bash
Copy code
python manage.py createsuperuser
Run the Development Server

bash
Copy code
python manage.py runserver
Access the Application

Admin panel: http://127.0.0.1:8000/admin/
API endpoints: http://127.0.0.1:8000/api/