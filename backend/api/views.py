from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Wishlist
import json

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def example_view(request):
    return JsonResponse({"message": "API is working!"})


@csrf_exempt
def add_to_wishlist(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_name = data.get("product_name")
        price = data.get("price")
        image = data.get("image")

        if request.user.is_authenticated:
            Wishlist.objects.create(user=request.user, product_name=product_name, price=price, image=image)
            return JsonResponse({"success": True, "message": "Added to Wishlist!"})
        else:
            return JsonResponse({"success": False, "message": "User not authenticated."}, status=403)
    return JsonResponse({"success": False}, status=400)

def get_wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user).values("id", "product_name", "price", "image")
        return JsonResponse(list(wishlist_items), safe=False)
    return JsonResponse({"success": False, "message": "User not authenticated."}, status=403)

