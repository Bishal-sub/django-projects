from django.shortcuts import render
from django.db.models import Q
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    category = request.GET.get('category')
    query = request.GET.get('q')
   
    products = Product.objects.all()

    if category:
        products = Product.objects.filter(category__name__iexact=category)
   
    if query:
        products = products.filter(
            Q(productname__icontains = query) |
            Q(description__icontains = query) 
            
        )
    return render(request, 'home.html', {'products': products})

