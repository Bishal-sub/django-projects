from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.contrib import messages
from .models import Product, Cart, CartItem,ProductVariant,Size,Color
from django.contrib.auth.decorators import login_required
import random

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


def product_details(request, id):
    product = Product.objects.get(id=id)

    size_id = request.GET.get('size')
    color_id = request.GET.get('color')

    variants = product.variants.all()

    selected_variant = None

    # user selected variant
    if size_id and color_id:
        selected_variant = variants.filter(
            size_id=size_id,
            color_id=color_id
        ).first()

    # fallback 1: in-stock variant
    if not selected_variant:
        selected_variant = variants.filter(stock__gt=0).first()

    # fallback 2: ANY variant
    if not selected_variant:
        selected_variant = variants.first()

    # FINAL SAFETY CHECK (IMPORTANT)
    if not selected_variant:
        selected_variant = None

    sizes = Size.objects.filter(productvariant__product=product).distinct()
    colors = Color.objects.filter(productvariant__product=product).distinct()

    return render(request, 'product_detail.html', {
        'product': product,
        'selected_variant': selected_variant,
        'sizes': sizes,
        'colors': colors,
    })


@login_required
def add_to_cart(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)

    
    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        variant=variant
    )

    if not created:
        item.quantity += 1

    # stock check
    if item.quantity > variant.stock:
        item.quantity = variant.stock

    item.save()

    return redirect('cart_view')


@login_required
def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()

    
    total = sum(item.total_price() for item in items)
    cart_count = sum(item.quantity for item in items)

    return render(request, 'cart.html', {
        'items': items,
        'total': total,
        'cart_count':cart_count
    })


@login_required
def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('cart_view')


@login_required
def update_quantity(request, item_id):
    item = CartItem.objects.get(id=item_id)
    qty = int(request.POST.get('quantity'))

    if qty > item.variant.stock:
        messages.error(request, f"Only {item.variant.stock} items available")
        return redirect('cart_view')

    if qty < 1:
        qty = 1

    item.quantity = qty
    item.save()

    return redirect('cart_view')

