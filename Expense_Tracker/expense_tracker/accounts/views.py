from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if User.objects.filter(username = username).exists():
            messages.error(request,"UserALready exist")
        
    
    
    
    
    
    
    return render(request,'register.html')