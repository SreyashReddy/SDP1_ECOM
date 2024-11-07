from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from product_app.models import Product
from .models import Wishlist
from django.contrib import messages

@login_required
def customer_dashboard(request):
    products = Product.objects.all()
    wishlist_products = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    context = {
        'products': products,
        'wishlist_count': len(wishlist_products),
        'wishlist_products': wishlist_products,
    }
    return render(request, 'customer_app/customer_dashboard.html', context)

@login_required
def add_to_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user,
            product=product
        )
        if created:
            messages.success(request, 'Product added to wishlist!')
        else:
            wishlist_item.delete()
            messages.info(request, 'Product removed from wishlist!')
    return redirect('customer_dashboard')