from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from auth_app.models import FarmerProfile, CustomerProfile
from product_app.models import Product
from order_app.models import Order

# Custom check to ensure only superusers can access the admin dashboard
def admin_check(user):
    return user.is_superuser

# Ensure the user is logged in and passes the admin check
@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    # Count the number of farmers, customers, products, and orders
    farmer_count = FarmerProfile.objects.count()
    customer_count = CustomerProfile.objects.count()
    product_count = Product.objects.count()  # Get the number of products
    order_count = Order.objects.count()  # Get the number of orders

    context = {
        'farmer_count': farmer_count,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }

    # Render the admin dashboard template
    return render(request, 'admin_app/admin_dashboard.html', context)


# View to list all farmers
@login_required
@user_passes_test(admin_check)
def farmer_list(request):
    farmers = FarmerProfile.objects.all()  # Get all farmers
    context = {
        'farmers': farmers,
    }
    return render(request, 'admin_app/farmer_list.html', context)


# View to list all customers
@login_required
@user_passes_test(admin_check)
def customer_list(request):
    customers = CustomerProfile.objects.all()  # Get all customers
    context = {
        'customers': customers,
    }
    return render(request, 'admin_app/customer_list.html', context)


# View to list all products
@login_required
@user_passes_test(admin_check)
def product_list(request):
    products = Product.objects.all()  # Get all products
    context = {
        'products': products,
    }
    return render(request, 'admin_app/product_list.html', context)


# View to list all orders
@login_required
@user_passes_test(admin_check)
def order_list(request):
    orders = Order.objects.all()  # Get all orders
    context = {
        'orders': orders,
    }
    return render(request, 'admin_app/order_list.html', context)
