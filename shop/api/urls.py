from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CartViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    path("cart/", CartViewSet.as_view({"get": "list"})),
    path("cart/add/<int:pk>/", CartViewSet.as_view({"post": "add"})),
    path("cart/update/<int:pk>/", CartViewSet.as_view({"patch": "update_quantity"})),
    path("cart/remove/<int:pk>/", CartViewSet.as_view({"delete": "remove"})),
    path("cart/clear/", CartViewSet.as_view({"delete": "clear"})),
]