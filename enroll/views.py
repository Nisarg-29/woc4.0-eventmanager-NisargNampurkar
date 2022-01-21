from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event


def img(request):
    template=loader.get_template('pexels-ovan-57690.jpg')
    context={
        
    }
    return HttpResponse(template.render(context,request))


def index(request):
    template=loader.get_template('home.html')
    context={
        
    }
    return HttpResponse(template.render(context,request))

def Regis(request):

    if request.method == 'POST':
        event=Event()
        event.Eventname=request.POST.get('Eventname')
        event.Desc= request.POST.get('Desc')
        event.inputAddress=request.POST.get('inputAddress')
        event.inputCity=request.POST.get('inputCity')
        event.inputState=request.POST.get('inputState')
        event.inputZip=request.POST.get('inputZip')
        event.Eventstart=request.POST.get('Eventstart')
        event.Eventstartt=request.POST.get('Eventstartt')
        event.Eventend=request.POST.get('Eventend')
        event.Eventendt=request.POST.get('Eventendt')
        event.Eventreg=request.POST.get('Eventreg')
        event.Eventregt=request.POST.get('Eventregt')
        event.inputEmail4=request.POST.get('inputEmail4')
        event.inputPassword4=request.POST.get('inputPassword4')
        event.save()
        return render(request, 'home.html')  

    template=loader.get_template('Eventreg.html')
    
    context={

    }

    return HttpResponse(template.render(context,request))

def partiRegis(request):
    events=Event.objects.all() 
    return render(request,'participantreg.html',{'events':events})

def dashboard(request):
    
    template=loader.get_template('Dashboard.html')
    
    context={

    }

    return HttpResponse(template.render(context,request))    
    
# Create your views here.
