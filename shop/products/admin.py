from django.contrib import admin

from .models import (
    Cart, CartItem, Category,
    Product, SubCategory
)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SubCategory)
