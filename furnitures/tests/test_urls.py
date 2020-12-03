from django.test import TestCase
from django.urls import reverse, resolve
from furnitures.views import product_detail, add_product, edit_product,\
    delete_product, all_products


class TestUrls(TestCase):

    def test_all_products_url_is_resolved(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)

    def test_product_detail_url_is_resolved(self):
        url = reverse('product_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_detail)

    def test_add_product_url_is_resolved(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)

    def test_edit_product_url_is_resolved(self):
        url = reverse('edit_product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_product)

    def test_delete_product_url_is_resolved(self):
        url = reverse('delete_product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_product)
