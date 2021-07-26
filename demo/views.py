from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Meetup, Participant, Quiz
from .forms import RegistrationForm, QuizForm

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

class IndexView(generic.ListView):
    model= Quiz
    template_name= 'demo/quiz.html'

    def get_queryset(self):
        return Quiz.objects.all()

    def my_form(request):
        if request.method=='POST':
            form=QuizForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                form=QuizForm()
            return render(request, 'demo/quiz.html', {'form': form})

class DetailView(generic.DetailView):
    model=Quiz

def confirm_registration(request, meetup_slug):
    meetup=Meetup.objects.get(slug=meetup_slug)
    return render(request, 'demo/registration-success.html',{
        'organizer_email': meetup.organizer_email
    })