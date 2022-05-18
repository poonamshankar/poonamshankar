from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.floor)
admin.site.register(models.rooms_type)
admin.site.register(models.rooms)
admin.site.register(models.booking)
