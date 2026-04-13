from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    return render(request,'profile.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
        else:
            messages.error(request, "Please correct the error below")
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})    
        
            
            
            