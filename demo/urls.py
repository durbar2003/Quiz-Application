from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.index, name='all-meetups'),
    path('demo/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('demo/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),
]