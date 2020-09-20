# Setting up the Project
* pip install virtualenv
* virtualenv venv
* cd venv
* cd Scripts
* activate
* pip install django==2.2.8

## Starting the Project
* django-admin startproject BuildForAssam
* cd BuildForAssam
* python manage.py startapp Inventory
* python manage.py runserver ctrl+c to stop
* python manage.py migrate
* python manage.py createsuperuser (name)
* python manage.py runserver
