from django.contrib import admin
from django.urls import path
from.import views

urlpatterns=[
    path('slice',views.slice, name='sl'),
    path('login', views.login_view, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.log_out, name="logout"),
    
    path('floor', views.all_floors, name="floor"),
    path('add_floor', views.add_floor, name="add_floor"),
    path('edit_floor/<int:id>', views.edit_floor, name="edit_floor"),
    path('delete_floor/<int:id>',views.delete_floor, name="delete_floor"),
   
    path('rooms_types', views.all_rooms_type, name="rooms_type"),
    path('add_room_type', views.add_room_type,name="add_room_type"),
    path('edit_room_type/<int:id>', views.edit_room_type, name="edit_room_type"),
    path('delete_room_type/<int:id>', views.delete_room_type, name="delete_room_type"),
    
    path('rooms_information',views.rooms_information, name="rooms_information"),
    path('add_room', views.add_room, name="add_room"),
    path('edit_room/<int:id>', views.edit_room, name = 'edit_room'),
    path('delete_room/<int:id>', views.delete_room, name = "delete_room"),
    
    
    
]