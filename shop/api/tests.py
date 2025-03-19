from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from products.models import (
    Cart, CartItem, Category,
    Product, SubCategory
)


class ShopAPITestCase(TestCase):
    def setUp(self):
        """Создание тестовых данных перед каждым тестом."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")
        self.category = Category.objects.create(
            name="Фрукты", slug="fruits")
        self.subcategory = SubCategory.objects.create(
            name="Цитрусовые", slug="citrus", category=self.category)
        self.product = Product.objects.create(
            name="Апельсин",
            slug="orange",
            price=100.00,
            subcategory=self.subcategory,
            image_small="products/small/orange.jpg",
            image_medium="products/medium/orange.jpg",
            image_large="products/large/orange.jpg",
        )

    def test_get_categories(self):
        """Тест получения списка категорий."""
        response = self.client.get("/api/v1/categories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "Фрукты")

    def test_get_products(self):
        """Тест получения списка товаров."""
        response = self.client.get("/api/v1/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "Апельсин")

    def test_add_to_cart(self):
        """Тест добавления товара в корзину."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post(f"/api/v1/cart/add/{self.product.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Cart.objects.filter(user=self.user).exists())
        self.assertTrue(CartItem.objects.filter(
            cart__user=self.user, product=self.product).exists())

    def test_clear_cart(self):
        """Тест очистки корзины."""
        self.client.force_authenticate(user=self.user)
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product=self.product, quantity=1)

        response = self.client.delete("/api/v1/cart/clear/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CartItem.objects.filter(
            cart__user=self.user).count(), 0)