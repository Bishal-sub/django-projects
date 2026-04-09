from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','img']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    model = User
    fields = ('email','username','password1','password2')
        