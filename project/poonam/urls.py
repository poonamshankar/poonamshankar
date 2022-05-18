from django.contrib import admin
from django.urls import path
from.import views

urlpatterns=[
    path('slice',views.slice, name='sl'),
    path('login', views.login_view, name="login"),
    path('logout',views.log_out, name="logout"),
    path('floor', views.all_floors, name="floor"),
    path('add_floor', views.add_floor, name="add_floor"),
    path('edit_floor/<int:id>', views.edit_floor, name="edit_floor"),
    path('register',views.register, name="register"),
]