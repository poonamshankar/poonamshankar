from unicodedata import name
from django.shortcuts import render
from .models import floor, rooms, rooms_type, booking, User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def slice(request):
    return render(request,'poonam/layout.html')

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

    

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("floor"))
        else:
            return render(request, "poonam/login.html",
         {"message": "Invalid username and/or password."
        })
    else:
        return render(request, "poonam/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "poonam/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "poonam/register.html", {
                "message": "Username already taken."
            })
        return render(request, 'poonam/register.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "poonam/register.html")

def all_floors(request):
    floors = floor.objects.all()
    return render(request, 'poonam/floors.html', {'floors': floors})

def add_floor(request):
    if request.method == "POST":
        name = request.POST["name"] 
        try:
            a = floor(floor = name)
            a.save()
        except:
            return render(request, 'poonam/add_floor.html',{"message":'Try Again'})
        return HttpResponseRedirect(reverse('floors'))    
    else:
        return render(request, 'poonam/add_floor.html')

def edit_floor(request, id):
    singleFloor = floor.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["edit_floor"]
        singleFloor.floor_name = name
        try:
            singleFloor.save()
        except:
            return render(request, "poonam/edit_floor.html", {'singleFloor': singleFloor 'message':'please try again'})
        return HttpResponseRedirect(reverse('floor'))
    else:
        return render(request, "poonam/edit_floor.html")


def delete_floor(request, id):
    delete = floor.objects.get(id=id)
    floors = floor.objects.all()
    try:
        delete.delete()
    except:
           return render(request, 'poonam/floors.html',{'floors':floors}) 
    return HttpResponseRedirect(reverse('floors'))       
