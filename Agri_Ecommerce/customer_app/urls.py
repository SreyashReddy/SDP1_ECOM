from django.urls import path
from .views import customer_dashboard,add_to_cart,view_cart,add_to_wishlist,view_wishlist,remove_from_cart
urlpatterns = [
    path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='customer_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', view_wishlist, name='customer_wishlist'),
]