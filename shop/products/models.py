from django.db import models
from django.contrib.auth.models import User

from .constants import DEF_QUANTITY, MAX_PRICE, NAME_LENGTH, PRICE_DIGTS


class Category(models.Model):
    name = models.CharField(
        max_length=256, unique=True
    )
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to='categories/'
    )

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='subcategories'
    )
    name = models.CharField(
        max_length=NAME_LENGTH, unique=True
    )
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to='subcategories/'
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(
        SubCategory, on_delete= models.CASCADE,
        related_name='products'
    )
    name = models.CharField(
        max_length=NAME_LENGTH, unique=True
    )
    slug = models.SlugField(unique=True)
    price = models.DecimalField(
        max_digits=MAX_PRICE, decimal_places=PRICE_DIGTS
    )
    image_small = models.ImageField(
        upload_to='products/small/'
    )
    image_medium = models.ImageField(
        upload_to='products/medium'
    )
    image_large = models.ImageField(
        upload_to='products/large/'
    )

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='cart'
    )
    products = models.ManyToManyField(
        Product, through='CartItem'
    )

    def __str__(self):
      return f'Корзина пользователя {self.user.username}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=DEF_QUANTITY)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
