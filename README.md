> <p align="center"> Django App to track the Receipts</p>
> Objective:
> Create a simple Django application that allows users to manually enter and track their receipt information. This application should focus on basic CRUD (Create, Read, Update, Delete) operations and user authentication.
Requirements:

A. Models:
1. Receipt: Should include fields like store name, date of purchase, item list (simple text field), and total amount.
2. User: Utilize Django's built-in User model for linking receipts to users.

B. Views and Templates:
1. List View: Display a list of receipts submitted by the logged-in user.
2. Detail View: Show detailed information about each receipt when selected.
3. Form View: A form to submit new receipts and edit existing ones.

C. User Authentication:
1. Implement functionalities for user registration, login, and logout.
2. Ensure users can only view and manage their own receipts.

D. Forms:
- Use Django forms for the submission and editing of receipt details.

E. Testing:
- Write basic tests for your models and views.

> ### <p align="center">Installation</p>
> 
* To make this application work follow these steps:

1. Download the project form github repo:
   * https://github.com/SaberHardy/RecieptTracker
2. cd open the terminal where it downloaded:
  - cd RecieptTracker
3. create the virtual environment
   * python -m venv venv
4. activate the venv
   * .\venv\Scripts\activate
5. install requirements
   * pip install -r requirements.txt
### NOTE: the python version should be compatible with django

6. migrate the database:
   * python manage.py makemigrations
   * python manage.py migrate
7. Run the server
   * python manage.py runserver
