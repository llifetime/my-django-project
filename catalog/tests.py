from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Product


class CatalogTestCase(TestCase):
    def setUp(self):
        """Настройка тестовых данных"""
        self.client = Client()
        self.category = Category.objects.create(
            name='Тестовая категория',
            description='Описание тестовой категории'
        )
        self.product = Product.objects.create(
            name='Тестовый товар',
            description='Описание тестового товара',
            category=self.category,
            price=1000.00
        )

    def test_home_page(self):
        """Тест домашней страницы"""
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/home.html')
        self.assertContains(response, 'Добро пожаловать')

    def test_contacts_page(self):
        """Тест страницы контактов"""
        response = self.client.get(reverse('catalog:contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/contacts.html')
        self.assertContains(response, 'Наши контакты')

    def test_category_creation(self):
        """Тест создания категории"""
        category = Category.objects.get(name='Тестовая категория')
        self.assertEqual(category.name, 'Тестовая категория')
        self.assertEqual(str(category), 'Тестовая категория')

    def test_product_creation(self):
        """Тест создания товара"""
        product = Product.objects.get(name='Тестовый товар')
        self.assertEqual(product.name, 'Тестовый товар')
        self.assertEqual(product.price, 1000.00)
        self.assertEqual(product.category, self.category)
        self.assertTrue(product.is_published)

    def test_product_str_method(self):
        """Тест строкового представления товара"""
        product = Product.objects.get(name='Тестовый товар')
        expected_str = 'Тестовый товар - 1000.00 руб.'
        self.assertEqual(str(product), expected_str)


class ModelRelationsTestCase(TestCase):
    def test_product_category_relation(self):
        """Тест связи товара с категорией"""
        category = Category.objects.create(name='Категория 1')
        product = Product.objects.create(
            name='Товар 1',
            category=category,
            price=500.00
        )

        self.assertEqual(product.category, category)
        self.assertIn(product, category.products.all())


class TemplateTestCase(TestCase):
    def test_base_template_extends(self):
        """Тест наследования шаблонов"""
        response = self.client.get(reverse('catalog:home'))
        self.assertContains(response, 'My Catalog')
        self.assertContains(response, 'navbar')
        self.assertContains(response, 'bootstrap')