from django.shortcuts import render
from .models import floor, rooms, rooms_type, booking, User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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
            if user.is_superuser:
                login(request, user)
                return HttpResponseRedirect(reverse("floor"))
            else:
                return render(request, "poonam/login.html", {"message": "not admin."})
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
        confirmation = request.POST["conform_password"]
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

@login_required(login_url="poonam/login")
def all_floors(request):
    floors = floor.objects.all()
    return render(request, 'poonam/floors.html', {'floors': floors})

def add_floor(request):
    if request.method == "POST":
        name = request.POST["name"] 
        try:
            a = floor(floor_name = name)
            a.save()
        except:
            return render(request, 'poonam/add_floor.html',{"message":'Try Again'})
        return HttpResponseRedirect(reverse('floor'))    
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
            return render(request, "poonam/edit_floor.html", {'singleFloor': singleFloor, 'message':'please try again'})
        return HttpResponseRedirect(reverse('floor'))
    else:
        return render(request, "poonam/edit_floor.html", {'singleFloor': singleFloor})


def delete_floor(request, id):
    delete = floor.objects.get(id=id)
    floors = floor.objects.all()
    try:
        delete.delete()
    except:
           return render(request, 'poonam/floors.html',{'floors':floors}) 
    return HttpResponseRedirect(reverse('floor')) 


def all_rooms_type(request):
    rooms = rooms_type.objects.all()
    return render(request, 'poonam/room_type.html',{'rooms':rooms})


def add_room_type(request):
    if request.method == "POST":
       name = request.POST["type"]
    #    Ac_room = request.POST["Ac_room"]
    #    without_Ac = request.POST[]
       try:
           a = rooms_type(type_name = name)
           a.save()
       except:
           return render(request, 'poonam/add_room_type.html',{"message":'Try Again'})
       return HttpResponseRedirect(reverse('rooms_type'))    
    else:
        return render(request, 'poonam/add_room_type.html')
  

def edit_room_type(request,id):
    room = rooms_type.objects.get(id=id)
    if request.method=="POST":
       name= request.POST["edit_room_type"]
       room.type_name= name
       try:  
            room.save()
       except:
        return render(request, "poonam/edit_room_type.html", {'rooms':room , 'message':'please try again'})
       return HttpResponseRedirect(reverse('rooms_type'))
    else:
     return render(request, "poonam/edit_room_type.html",{'rooms':room})


def delete_room_type(request, id):
    delete = rooms_type.objects.get(id=id)
    rooms = rooms_type.objects.all()
    try:
        delete.delete()
    except:
        return render(request, 'poonam/room_type.html',{'rooms':rooms}) 
    return HttpResponseRedirect(reverse('rooms_type'))


def rooms_information(request):
    room_information =rooms.objects.all()
    return render(request, 'poonam/all_rooms.html',{'room_information': room_information})



def add_room(request):
    floors_data = floor.objects.all()
    typeData = rooms_type.objects.all()
    if (request.method == 'POST'):
        # floor_id = request.POST['']
        floor_id = request.POST['floors']
        type_id = request.POST['types']
        room_nos = request.POST['no']
        cost = request.POST['cost']
        availiblitys = request.POST['availibility']
        sel_floor = floor.objects.get(id=floor_id)
        type_room = rooms_type.objects.get(id=type_id)
        # print(room_nos, cost, availiblitys, sel_floor.floor_name, type_room.type_name)
        a = rooms(room_no = room_nos, type_id = type_room, room_cost = cost, floor_id = sel_floor, availibility = availiblitys)
        try:
           a.save()
        except:
            return render(request, 'poonam/add_room.html',{'floors': floors_data, 'types': typeData,  "message":'Try Again'})
        return HttpResponseRedirect(reverse('rooms_information'))   
    #     a = rooms(room_no = room_nos, type_name_id = type_room, room_cost = cost, floor_id = sel_floor, availibility = availiblitys)
    #     a.save()
    #     # try:
            
    #     # except:
    #     #     return render(request, 'poonam/add_room.html',{'floors': floors_data, 'types': typeData,  "message":'Try Again'})
    #     return HttpResponseRedirect(reverse('rooms_information'))
    else:
        return render(request, 'poonam/add_room.html', {'floors': floors_data, 'types': typeData})

           

    




