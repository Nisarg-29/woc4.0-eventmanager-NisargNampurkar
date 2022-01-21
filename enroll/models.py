from django.db import models

# Create your models here.

class Participant(models.Model):
    name=models.CharField(max_length=100, unique=True)
    Email=models.EmailField()
    contact=models.CharField(max_length=100, unique=True)
    inlineRadio1=models.BooleanField()
    inlineRadio2=models.BooleanField()
    pno=models.PositiveIntegerField()


class Event(models.Model):
    Eventname=models.CharField(max_length=100, unique=True)
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

    