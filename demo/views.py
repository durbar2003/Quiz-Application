from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant, Quiz
from .forms import RegistrationForm

# Create your views here.
def index(request):
    meetups=Meetup.objects.all()
    return render(request, 'demo/index.html', {
        'meetups':meetups
        })
def meetup_details(request, meetup_slug):
        selected_meetup= Meetup.objects.get(slug=meetup_slug)
        try:
            if request.method=='GET':
                registration_form=RegistrationForm()
                
            else:
                registration_form=RegistrationForm(request.POST)
                if registration_form.is_valid():
                    user_email= registration_form.cleaned_data['email']
                    participant, _= Participant.objects.get_or_create(email=user_email)
                    selected_meetup.participants.add(participant)
                    return redirect('confirm-registration', meetup_slug=meetup_slug)


            return render(request, 'demo/meetup_details.html', {
                    'meetup_found':True,
                    'meetup': selected_meetup,
                    'form':registration_form
        })
        except Exception as exc:
            return render(request, 'demo/meetup_details.html',{
                'meetup_found':False
        })

def qpage(request):
    questions=Quiz.objects.all()
    return render(request, 'meetup_details.html', { 'questions' : questions})

def confirm_registration(request, meetup_slug):
    meetup=Meetup.objects.get(slug=meetup_slug)
    return render(request, 'demo/registration-success.html',{
        'organizer_email': meetup.organizer_email
    })