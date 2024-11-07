from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from product_app.models import Product

# View to add products to the cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if product already exists in the user's order
    order_item, created = Order.objects.get_or_create(user=request.user, product=product, payment_status='Pending')

    # If the item is already in the cart, increase the quantity
    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('customer_dashboard')  # Redirect back to the customer dashboard


# View to display the user's cart
@login_required
def view_cart(request):
    # Retrieve all pending orders for the logged-in user
    orders = Order.objects.filter(user=request.user, payment_status='Pending')

    # Calculate the total price for each order
    total_price = sum(order.product.price * order.quantity for order in orders)

    context = {
        'orders': orders,
        'total_price': total_price,
    }
    return render(request, 'order_app/cart.html', context)


# View to handle checkout
@login_required
def checkout(request):
    orders = Order.objects.filter(user=request.user, payment_status='Pending')
    total_price = sum(order.product.price * order.quantity for order in orders)

    # Mock payment URL (replace this with an actual payment gateway)
    payment_url = f"https://paymentgateway.com/pay?amount={total_price}&user_id={request.user.id}"
    return redirect(payment_url)


# View to handle successful payment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_success(request):
    order_ids = request.GET.getlist('order_ids', [])
    orders = Order.objects.filter(id__in=order_ids, user=request.user, payment_status='Pending')

    # Mark the orders as paid
    for order in orders:
        order.payment_status = 'Paid'
        order.save()

    return render(request, 'order_app/order_success.html', {'orders': orders})


# View to handle payment failure
@csrf_exempt
def payment_failure(request):
    return render(request, 'order_app/payment_failure.html')
