# Sipmle-Django-Todo-upload-Photo-App
A simple todo and upload photo app built with django


### Setup
To get this repository, run the following command inside your git enabled terminal

```bash
git clone https://github.com/shreys7/django-todo.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command.
```bash
python manage.py migrate
```

One last step Create a super user with following code.
```bash
python manage.py createsuperuser
```

To run this app, open terminal in that folder and run the following command.

```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/ for the App.

Since you are not yet a user, you will be redirected to the Sign Up page.  By filling out the form that opens, you will be directed to the Login page after registering. When you fill out the login page with your user information, you will reach the Homepage page opened for you. On this page, you can list, add, update, or delete things to do using the todo tab. On the second tab, the Photos tab, you can add or delete photos you want to save. Enjoy Tamemen is an open source code :)
