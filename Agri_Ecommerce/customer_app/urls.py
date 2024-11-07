from django.urls import path
from .views import customer_dashboard,add_to_cart,view_cart,add_to_wishlist
urlpatterns = [
    path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='customer_cart'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),

]