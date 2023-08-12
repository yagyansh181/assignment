# Housr Management System

The Housr Management System is a web application designed to help manage community residents, employees, events, and permissions. It provides a user-friendly interface for administrators to manage different aspects of the community.

## Features

- Manage residents' information, contracts, and move-in/move-out dates.
- Assign groups and permissions to employees for role-based access control.
- Organize and schedule community events.
- Integration with the Django Admin panel for easy management.

## Getting Started

### Prerequisites

- Python 3.10
- Django (version 4.2.4)

### Run Project At:
[Housr Management](yagyansh.pythonanywhere.com)

## Screenshots
### Homepage
![Homepage](images/homepage.png)
### Admin
![Admin Panel](images/admin_panel.png)
### Dashboard Panels
![Admin Dashboard](images/dash.png)
![Employee Panel](images/employee.png)
![Resident Panel](images/resident_panel.png)
![Create Permissions Panel](images/permission.png)
![Community Event Panel](images/event.png)


## Installation Guide

0) Clone the repository:

   ```sh
   git clone https://github.com/yagyansh181/assignment
   cd your-repo

1) Install project dependencies:
    ```sh
    pip install -r requirements.txt

Configure the database settings in settings.py.

2) Apply database migrations:
    ```sh
    python manage.py makemigrartions
    python manage.py migrate

3) Create a superuser to access the admin interface:
     ```sh
    python manage.py createsuperuser

4) Start the development server:
    ```sh
    python manage.py runserver

### Usage
Visit the homepage at http://127.0.0.1:8000/ to access the application.
Use the "Go to Admin" button to access the Django Admin panel at http://127.0.0.1:8000/admin/.




