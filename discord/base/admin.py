from django.contrib import admin

# Register your models here.

# import the room table/model
from .models import Room, Topic, Message

# register the room table/model
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
