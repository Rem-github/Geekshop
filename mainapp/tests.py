from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from mainapp.models import ProductCategory, Product


class TestMainSmokeTest(TestCase):

    def setUp(self):
        category = ProductCategory.objects.create(
            name = 'TestCategory'
        )
        Product.objects.create(
            category=category,
            name='product_test_1',
            price=100,

        )
        self.client=Client()

    def tearDown(self):     # для удаления всего, кроме данных базы. Картинки, например, которые
                            # подгружаются в тестовом режиме и оседают в локальных папаках
        pass

    def test_product_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_products_product(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/product/{product_item.pk}/')
            self.assertEqual(response.status_code, 200)
