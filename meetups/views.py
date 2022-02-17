from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import RegistrationForm
# Create your views here.

def index(request):
    meetups=Meetup.objects.all()

    # meetups=[
    #     {
    #         'title': 'A First Meetup ',
    #         'location':'dhaka',
    #         'date':'12/12/2012',
    #         'slug':'first-meetup'},
    #     {
    #         'title': 'A second Meetups',
    #         'location':'chittagong',
    #         'date':'12/12/2021',
    #         'slug':'second-meetup'
    #         }
    # ]

    return render(request,'meetups/index.html',{
        
        'meetups': meetups
        })

def meetup_details(request,meetup_slug):
    print(meetup_slug)
    
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        if request.method=='GET':
            
            registration_form=RegistrationForm()
            
        else:
            registration_form=RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')
        return render(request,'meetups/meetup-details.html',{
                'meetup':selected_meetup,
                'form':registration_form,
                'meetup_title':selected_meetup.title,
                'meetup_description':selected_meetup.description,
                'meetup_slug':selected_meetup.slug ,
                'meetup_found':True,
            })


    except Exception as exc:
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':True})

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')
