from django.shortcuts import render
from .models import floor, rooms, rooms_type, booking
from django.contrib.auth import authenticate,login
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def slice(request):
    return render(request,'poonam/layout.html')

def log_out(request):
    return render(request, 'poonam/logout.html')    

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
            return HttpResponseRedirect(reverse("index"))
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
    return render(request, 'poonam/add_floor.html')

def edit_floor(request, id):
    singleFloor = floor.objects.get(id=id)
    return render(request, "poonam/add_floor.html", {'singleFloor': singleFloor})