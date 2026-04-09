from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login

# Create your views here.

def home(request):
    
    return render(request,'home.html')

def register(request):
    
    if request.method == "post":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    
    return render(request,'register.html',{'form':form})