# Onspec_Task
# Onspec Task – Job_candidate_management_system

## TASK DESCRIPTION

This is a **Django REST API** that stores or updates job candidate contact information.

- If the email **does not exist**, create a new candidate.
- If the email **already exists**, update the existing candidate’s info.

**Frontend will be added later.**

---

## HOW TO RUN THE PROJECT

Follow these steps *exactly* to get the server running. Don’t skip anything.

**Step 1: Clone the repository**

git clone https://github.com/ahmedootta/Onspec_Task.git
cd Onspec_task

**Step 2: Create a virtual environment**
Linux/macOS: 

python3 -m venv venv
source venv/bin/activate

**Step 3: Install dependencies from requirements.txt**

pip install -r requirements.txt

**Step 4: Navigate to the Django project folder**

cd backend

**Step 5: Apply migrations to set up the database**

python3 manage.py makemigrations
python3 manage.py migrate

**Step 6: Run the development server**

python3 manage.py runserver

Now open your browser and go to: http://127.0.0.1:8000/

**To run tests:**

python manage.py test candidates
