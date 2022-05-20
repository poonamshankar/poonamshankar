from django.contrib import admin
from django.urls import path
from.import views

urlpatterns=[
    path('slice',views.slice, name='sl'),
    path('login', views.login_view, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.log_out, name="logout"),
    path('floor', views.all_floors, name="floor"),
    path('add_floor/<int:id>', views.add_floor, name="add_floor"),
    path('edit_floor/<int:id>', views.edit_floor, name="edit_floor"),
    path('delete',views.delete_floor, name="delete_floor"),
]