from .models import Wishlist, CartItem

def wishlist_and_cart_counts(request):
    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
        cart_items_count = CartItem.objects.filter(user=request.user).count()
    else:
        wishlist_count = 0
        cart_items_count = 0

    return {
        'wishlist_count': wishlist_count,
        'cart_items_count': cart_items_count,
    } 