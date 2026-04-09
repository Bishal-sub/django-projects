from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweet
from .form import TweetForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def Tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit= False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
            
    else:
        form = TweetForm()
    
    return render(request,'create_tweet.html',{'form':form}) 
@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES , instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
        
    return render(request,'create_tweet.html',{'form':form})         

@login_required
def delete_tweet(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list') 
    
    return render(request,'confirm_delete.html',{'tweet':tweet})   


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')
        else:
            print("ERRORS:", form.errors)  # 👈 THIS LINE

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
      
        
    