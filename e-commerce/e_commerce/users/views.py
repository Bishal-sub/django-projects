from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            redirect('home')
            
        else:
            messages.error(request,"please correct the error below")
        
    else:
        form = SignUpForm()
        
        
    return render(request,'registration/signup.html',{'form':form})        
        
            
            
            