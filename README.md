# Setup Instructions
### Prerequisites
- **Python 3.7 or higher**
- **Django 3.2 or higher**
- **Django REST framework**
- **MySQL**

## Installation
`1.Clone the repository:`

```bash
git clone https://github.com/Prohlad99/teamcollab.git
cd teamcollab
```
`2.Create and activate a virtual environment:`
```bash
python -m venv venv
source venv\Scripts\activate
```
`3.Install the required packages:`
```bash
pip install -r requirements.txt
or
pip install django djangorestframework mysqlclient djangorestframework-simplejwt
```
`4.Set up your MySQL database:`
```bash
CREATE DATABASE teamcollab_db;
```

`5.Configure your database settings in settings.py:`
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'teamcollab_db',
        'USER': 'root',  # or your MySQL username
        'PASSWORD': '',  # or your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
`6.Apply migrations:`
```bash
python manage.py makemigrations
python manage.py migrate
```

`7.Create a superuser:`
```bash
python manage.py createsuperuser
```

`8.Run the development server:`
```bash
python manage.py runserver
```
# API Endpoints
### Users
- **Register User**
- **URL: /api/users/register/**
- **Method: POST**
- **Request Body:**
```json
{
    "username": "prohlad_mandal",
    "email": "prohlad.m99@gmail.com",
    "password": "1234",
    "first_name": "Prohlad",
    "last_name": "Mandal"
}
```
### Login User
- **URL: /api/users/login/**
- **Method: POST**
- **Request Body:**
```json
{
    "username": "prohlad_mandal",
    "password": "1234"
}
```

### Get User Details
- **URL: /api/users/{id}/**
- **Method: GET**
- **Headers:**
```bash
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Others API end point will be same as `Get User Details` that means you have add `access token` inside the headers.

# Others API end points are:
### _Users_
- **`Register User(POST):` _/api/users/register/_**
- **`Login User(POST):` _/api/users/login/_**
- **`Get User Details(GET):` _/api/users/{id}/_**
- **`Update User(PUT):` _/api/users/{id}/_**
- **`Delete User(DELETE)`: _/api/users/{id}/_**

### _Projects_
- **`List Projects(GET):` _/api/projects/_**
- **`Create Project(POST):` _/api/projects/_**
- **`Retrieve Project(GET)`: _/api/projects/{id}/_**
- **`Update Project(PUT)`: _/api/projects/{id}/_**
- **`Delete Project(DELETE)`: _/api/projects/{id}/_**

### _Tasks_
- **`List Tasks(GET):` _/api/projects/{project_id}/tasks/_**
- **`Create Task(POST):` _/api/projects/{project_id}/tasks/_**
- **`Retrieve Task(GET):` _/api/tasks/{id}/_**
- **`Update Task(PUT):` _/api/tasks/{id}/_**
- **`Delete Task(DELETE):` _/api/tasks/{id}/_**

### _Comments_
- **`List Comments(GET):` _/api/tasks/{task_id}/comments/_**
- **`Create Comment(POST):` _/api/tasks/{task_id}/comments/_**
- **`Retrieve Comment(GET):` _/api/comments/{id}/_**
- **`Update Comment(PUT):` _/api/comments/{id}/_**
- **`Delete Comment(DELETE):` _/api/comments/{id}/_**

### _You can check insomnia json file and test all api end point._