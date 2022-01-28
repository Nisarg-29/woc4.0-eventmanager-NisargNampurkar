from asyncio.windows_events import NULL
from enum import unique
from pickle import TRUE
from django.db import models


# Create your models here.




class Event(models.Model):
    Eventname=models.CharField(max_length=100, unique=False)
    Desc= models.TextField()
    inputAddress=models.TextField()
    inputCity=models.CharField(max_length=100, unique=False)
    inputState=models.CharField(max_length=100, unique=False)
    inputZip=models.CharField(max_length=100, unique=False)
    Eventstart=models.DateField()
    Eventstartt=models.TimeField()
    Eventend=models.DateField()
    Eventendt=models.TimeField()
    Eventreg=models.DateField()
    Eventregt=models.TimeField()
    inputEmail4=models.EmailField()
    inputPassword4=models.CharField(max_length=10, unique=False)

class Participant(models.Model):
    name=models.CharField(max_length=100, unique=True)
    Email=models.EmailField()
    contact=models.CharField(max_length=100, unique=False)
    eventID=models.CharField(max_length=100, unique=False)
    inlineRadio1=models.CharField(max_length=100, unique=False)
    pno=models.PositiveIntegerField(default=1)    