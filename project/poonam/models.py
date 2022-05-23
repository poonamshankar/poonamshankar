from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
 
class User(AbstractUser):
     pass


class floor(models.Model):
    floor_name = models.IntegerField(unique=True)


class rooms_type(models.Model):
    type_name = models.CharField(max_length=20)



class rooms(models.Model):
    room_no = models.IntegerField()
    type_id = models.ForeignKey(rooms_type,on_delete=models.CASCADE, related_name="type_id")
    room_cost = models.IntegerField()
    floor_id = models.ForeignKey(floor,on_delete=models.CASCADE, related_name="floor_id")
    availibility = models.CharField(max_length=50)
    
    

class booking(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_id")
    room_id = models.ForeignKey(rooms,on_delete=models.CASCADE, related_name="room_id")
    booking_date = models.DateTimeField(auto_now_add=True)
    expected_checkOut_date = models.DateTimeField(auto_now_add=True)
    no_of_staying_day = models.CharField(max_length=40)
    status = models.CharField(max_length=70)