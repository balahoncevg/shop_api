from rest_framework import serializers

from products.models import (
    Cart, CartItem, Category,
    Product, SubCategory
)


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "image", "subcategories"]

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        return SubCategorySerializer(subcategories, many=True).data


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "category", "name", "slug", "image"]


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "subcategory",
                  "price", "image_small", "image_medium", "image_large"]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "total_price"]

    def get_items(self, obj):
        items = obj.cartitem_set.all()
        return CartItemSerializer(items, many=True).data

    def get_total_price(self, obj):
        return sum(
            (item.product.price * item.quantity for
             item in obj.cartitem_set.all()))