# woc4.0-eventmanager-NisargNampurkar

The folder eventmanager contains the codes/components of MyEventManager web application made using django web framework.
This is my project on Event Manager web application.

The main functionalities include:

1)An organiser/host can register an event.

2)A participant can register for that event that has been registered by any organiser and which is open for registration(the deadline has not passed).

3)The organiser/host can retrieve all details about the participants registered for their event at any point of time which needs authentication.

Project Components and properties/constraints/criterias implemented:

1)A base html templates and other templates which are made to extend it.

2)Home page - link to the other sites. E.g. Event Registration, Participant Registration, Event Dashboard.

3)Event Registration - Organiser can register for an Event using this site. Event can be registered only once. E.g. Event with same name, and clashing event dates, location can't be registered. All the fields, except description are mandatory else the form will not get submitted. The host/organiser will receive the details of the registration through an email on the host email id (s)he provides and a unique event id(auto generated) for his/her just registered event. Some obvious criterias like event start time should be earlier than end time, clashing events can't have same names,etc must be followed or registeration will be unsuccessful and error message will be received.

4)Participant Registration - Participant can register for Registered Event using this site. This site will only shows those events for which Registration Deadline has not passed yet and one can register for only these events. Participant can only register one event at a time, and (s)he can't register for the same event twice. All the fields are mandatory else the form will not get submitted. On submitting, (s)he will receive an email on the email id (s)he provides and an SMS on the contact number (s)he provides. It will contain the details of the event registered to and a unique participant ID for that event.

5)Event Dashboard - An organiser can see the Partipants details which have created by them. Authentication required Event ID (which is unique for all events and created by Django backend) and password which has used by Organiser at the time of registering the Event.

The success messages will be displayed on the webite on successful registration or authentication and error messages depending upon which of the above condition is failing. 

Notifications:
Organiser will get an Email notification only on successfully registered for the event.
Participant will get Email and Message notification about their successful Registration.

Front-end:
Front-end is created using HTML, CSS and Javascript and it's a responsive website.

Please go through the demo Video of the working of the Web Application: https://drive.google.com/file/d/1lfgLue9TeqQwU8u_P9iIuB4meW4RLFEg/view

Video highlighting some of the obvious Criterias to be followed while registration or authentication: https://drive.google.com/file/d/1uo3--2UAZ24hVJVQ3p4Zgf-1PZFjcuLi/view

