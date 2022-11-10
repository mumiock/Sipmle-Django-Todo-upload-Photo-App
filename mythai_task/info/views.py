
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage


User = get_user_model()

# Create your views here.


def index(request):
    if request.user.is_anonymous:                   # if user is anonymus we redirect url to signup page.
        return redirect('info/signup')
    if request.user.is_user:                        # if user is Logged in we redirect url to home page.
        return redirect(request, 'info/home')
    
    return redirect('info/signup')                  # any other situation we redirect url to home page.


def signup(request):                                # user signup view, we using unique username, email and password 
                                                    # to create a registered user.
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            

            # Creating a User  username and password format
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()

            # We are creating a new model in which we will communicate with other models so that there is no confusion.
            userinfo =  Userinfo(
                user=get_object_or_404(User, id=user.id),
                usn=username 
            )
            userinfo.save()
            # We create empty data by adding the user info object we created to other models. Let's see an empty index for testing purposes
            usn = get_object_or_404(Userinfo, usn=userinfo.usn)
            Task(  
                usn=usn
            ).save()
            Photo(  
                usn=usn
            ).save()
            return HttpResponseRedirect(reverse('home') )

    return render(request, 'info/signup.html')

# We protect all nodes including homepage with login required so that it cannot be accessed from outside without login.
@login_required() 
def home(request):
    
    return render(request, 'info/homepage.html')


# Todo page view.
@login_required()
def todo(request, username):
    # To get only the todos belonging to the user, we search the database according to the request user 
    # in username and send it to the frontend.
    user = User.objects.get(username=username)
    info = Userinfo.objects.get(user_id=user.id)
    todo_list = Task.objects.filter(usn=info.usn).order_by('-created_at') # sort by near date
    return render(request, 'info/todo.html', {'todo_list': todo_list})

# Todo Add node
@login_required()
def add(request, username):

    # To add todo to the user, we save it to the Task table with the user info object instance.
    user = User.objects.get(username=username)
    info = Userinfo.objects.get(user_id=user.id)
    title = request.POST['title']
    Task.objects.create(title=title,usn_id=info.usn)

    return HttpResponseRedirect(reverse('todo' ,args=(username,)) )

# Todo delete node
@login_required()
def delete(request, todo_id, username):
    # We delete the todo identified by the unique todo_id.
    todo = get_object_or_404(Task, pk=todo_id)
    todo.delete()

    return  HttpResponseRedirect(reverse('todo' ,args=(username,)) )

# Todo update node
@login_required()
def update(request, todo_id, username):
    # We update the todo identified by the unique todo_id. isCompleted or not.
    todo = get_object_or_404(Task, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return  HttpResponseRedirect(reverse('todo' ,args=(username,)) )

# Photo page view.
@login_required()
def photos(request, username):
    # To get only the photos belonging to the user, we search the database according to the request user 
    # in username and send it to the frontend.
    user = User.objects.get(username=username)
    info = Userinfo.objects.get(user_id=user.id)
    photo_list = Photo.objects.filter(usn=info.usn).order_by('-created_at') # sort by near date

    return render(request, 'info/photos.html', {'photo_list': photo_list })

# Photo add node
@login_required()
def photo_add(request, username):
    # First, we save the photo posted from html to the locale with the file system, 
    # then we save the database with the address of this file. Thus, we can render on the frontend using this path based on data. 
    # If privacy is a problem, the posted file can be encoded with base64 and saved to the database instead of the file system.
    user = User.objects.get(username=username)
    info = Userinfo.objects.get(user_id=user.id)

    upload = request.FILES['image']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)

    photo = Photo(image=file_url, usn_id=info.usn)
    photo.save()

    return HttpResponseRedirect(reverse('photos' ,args=(username,)) )

# Photo delete node
@login_required()
def photo_delete(request, photo_id, username):
    # We delete the todo identified by the unique photo_id.
    photo = get_object_or_404(Photo, pk=photo_id)
    photo.delete()

    return  HttpResponseRedirect(reverse('photos' ,args=(username,)) )

