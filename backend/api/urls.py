from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet
from . import views
from .views import add_to_wishlist, get_wishlist

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path("example/", views.example_view, name="example"),  
    path("add-to-wishlist/", add_to_wishlist, name="add_to_wishlist"),
    path("get-wishlist/", get_wishlist, name="wishlist"),
]

