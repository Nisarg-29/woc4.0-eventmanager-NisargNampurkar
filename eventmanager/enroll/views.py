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
        if event.Eventstart > event.Eventend or (event.Eventstart == event.Eventend and event.Eventstartt > event.Eventendt):
            messages.error(request, "Error! Event end time can't be earlier than start time. Please enter valid combination of dates")
            return render(request, 'home.html')  
        name=Event.objects.filter(Eventname=event.Eventname)
        for n in name:
            if str(n.Eventend) > event.Eventstart or (str(n.Eventend) == event.Eventstart and str(n.Eventendt) > event.Eventstartt):
                continue
            elif event.Eventend > str(n.Eventstart) or (event.Eventend == str(n.Eventstart) and event.Eventendt > str(n.Eventstartt)):
                continue
            else:
                messages.error(request,"Error! Another event with provided name is already scheduled during same timings.")
                return render(request, 'home.html')  
        event.save()

        #Body="Your Event is registered successfully.\nYour event ID is %s .\nHere is what we received from you:\n Eventname - %s \n Description - %s \n Venue - %s \n City - %s \n State - %s \n Zip - %s \n From - %s %s \n To - %s %s \n Registration Deadline - %s %s \n Host Email - %s \n Password - %s"%(Event.objects.latest('id').id,event.Eventname,event.Desc,event.inputAddress,event.inputCity,event.inputState,event.inputZip,event.Eventstart,event.Eventstartt,event.Eventend,event.Eventendt,event.Eventreg,event.Eventregt,event.inputEmail4,event.inputPassword4)
        #send_mail(
        #    'Success',
        #    Body,
        #    'managerevent15@gmail.com',
        #    [event.inputEmail4],
        #    fail_silently=False
        #)
        messages.success(request, "Registration successful" )
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
        if p.inlineRadio1=="Group":
            try:
                p.pno=request.POST.get("pno")
            except:
                p.pno=2
        else:
            p.pno=1   
        plist=Participant.objects.all()
        for P in plist:
            if (P.Email==p.Email and P.eventID==p.eventID):
                messages.error(request,"Error! You are already registered in this event.") 
                return render(request, 'home.html')             
        p.save()
        event=Event.objects.get(id=p.eventID)
        Body="Your registration for participation in out event %s is successful.\nYour unique ID as participant is %s. Here are the details of your event. \n Event ID - %s .\n Eventname - %s \n Description - %s \n Venue - %s \n City - %s \n State - %s \n Zip - %s \n From - %s %s \n To - %s %s \n"%(event.Eventname,Participant.objects.latest('id').id,event.id, event.Eventname,event.Desc,event.inputAddress,event.inputCity,event.inputState,event.inputZip,event.Eventstart,event.Eventstartt,event.Eventend,event.Eventendt)
        #send_mail(
        #    'Success',
        #    Body,
        #    'managerevent15@gmail.com',
        #    [p.Email],
        #    fail_silently=False
        #)
        
        #client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        #client.messages.create(to=p.contact,
        #                    from_=settings.TWILIO_NUMBER,
        #                    body=Body)
        messages.success(request, "Registration successful" )                    
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
        try:
            ev=Event.objects.get(id=eVentID)
            if ev.inputPassword4 == password:
                return render(request, 'Dashboard.html',{'plist':plist})
            else:
                messages.error(request,"Incorrect_Password")  
                return render(request, 'Dashboard.html')  
        except:
            messages.error(request,"No event with event ID you provided")
            return render(request, 'Dashboard.html')  

    return render(request, 'Dashboard.html')
    
# Create your views here.
