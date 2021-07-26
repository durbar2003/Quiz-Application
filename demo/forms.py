from django import forms
from .models import Quiz

class RegistrationForm(forms.Form):
    email=forms.EmailField(label='Your email')

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields=["ans"]
        labels={'ans': "Answer"}
