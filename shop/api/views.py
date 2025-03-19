from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



from products.models import (
    Cart, CartItem, Category,
    Product
)
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CartSerializer,
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.prefetch_related("subcategories").all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.select_related("subcategory").all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def add(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, pk=pk)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()
        return Response(CartSerializer(cart).data)

    @action(detail=True, methods=["patch"])
    def update_quantity(self, request, pk=None):
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, product_id=pk)
        item.quantity = request.data.get("quantity", item.quantity)
        item.save()
        return Response(CartSerializer(cart).data)

    @action(detail=True, methods=["delete"])
    def remove(self, request, pk=None):
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, product_id=pk)
        item.delete()
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=["delete"])
    def clear(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart.cartitem_set.all().delete()
        return Response({"message": "Cart cleared"})