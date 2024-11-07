from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem, Wishlist
from product_app.models import Product
from django.contrib import messages


@login_required
def customer_dashboard(request):
    products = Product.objects.all()  # Fetches all products
    # Cart and Wishlist Counts
    cart_items_count = CartItem.objects.filter(user=request.user).count()
    wishlist_count = Wishlist.objects.filter(user=request.user).count()

    # Get list of product IDs in user's wishlist
    wishlist_products = Product.objects.filter(wishlist__user=request.user)

    context = {
        'products': products,
        'cart_items_count': cart_items_count,
        'wishlist_count': wishlist_count,
        'wishlist_products': wishlist_products
    }
    return render(request, 'customer_app/customer_dashboard.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    # Increment quantity if the product is already in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('customer_dashboard')


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'customer_app/cart.html', {'cart_items': cart_items})


@login_required
def add_to_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

        if created:
            messages.success(request, 'Product added to wishlist!')
        else:
            wishlist_item.delete()
            messages.info(request, 'Product removed from wishlist!')

    return redirect('customer_dashboard')


@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'customer_app/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('customer_cart')
