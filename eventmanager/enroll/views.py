from asyncio.windows_events import NULL
import datetime
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from enroll.models import Event, Participant
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client

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

        str="Your Event is registered successfully.\nYour event ID is %s .\n"%(Event.objects.latest('id'))
        send_mail(
            'Success',
            str,
            'managerevent15@gmail.com',
            [event.inputEmail4],
            fail_silently=False
        )
        
        return render(request, 'home.html')  

    template=loader.get_template('Eventreg.html')
    
    context={

    }

    return HttpResponse(template.render(context,request))

def partiRegis(request):
    if request.method == "POST":
        p=Participant()
        p.name=request.POST.get("name")
        p.Email=request.POST.get("Email")
        p.contact=request.POST.get("contact")
        p.eventID=request.POST.get("inlineCheckbox1")
        p.inlineRadio1=request.POST.get("colorRadio1")
        p.inlineRadio2=request.POST.get("colorRadio1")
        if len(p.inlineRadio2)==0:
            try:
                p.pno=request.POST.get("pno")
            except:
                p.pno=2
        else:
            p.pno=1            
        p.save()
        str="Your are registered for the event %s successfully.\nYour event ID is %s .\n"%(Event.objects.get(id=p.eventID).Eventname,p.eventID)
        send_mail(
            'Success',
            str,
            'managerevent15@gmail.com',
            [p.Email],
            fail_silently=False
        )
        message_to_broadcast = ("U r registered successfully")
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        client.messages.create(to=p.contact,
                            from_=settings.TWILIO_NUMBER,
                            body=message_to_broadcast)
        return render(request, 'home.html')

    events=Event.objects.filter()
    events=Event.objects.all() 
    ev=[]
    for e in events:
        if e.Eventreg > datetime.date.today()  or (e.Eventreg == datetime.date.today() and e.Eventregt < datetime.datetime.now().time()):
            ev.insert(len(ev),e)          
    return render(request,'participantreg.html',{'events':ev})

def dashboard(request):
    
    if request.method == 'POST':
        eVentID=request.POST.get('eventID')
        password=request.POST.get('password')
        plist=Participant.objects.filter(eventID=eVentID)
        ev=Event.objects.get(id=eVentID)
        if ev:
            if ev.inputPassword4 == password:
                return render(request, 'Dashboard.html',{'plist':plist})
            else:
                return HttpResponse("Incorrect_Password\n")  
        else:
            return HttpResponse("No event with event ID you provided\n")

    return render(request, 'Dashboard.html')
    
# Create your views here.
