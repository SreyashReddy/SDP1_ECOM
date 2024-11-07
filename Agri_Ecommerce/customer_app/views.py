from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product_app.models import Product  # Ensure this import is correct


@login_required
def customer_dashboard(request):
    products = Product.objects.all()  # This fetches all products
    return render(request, 'customer_app/customer_dashboard.html', {'products': products})
