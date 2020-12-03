from django.test import TestCase
from django.urls import reverse, resolve
from services.views import services, edit_services, services_detail,\
    add_services, delete_services


class TestUrls(TestCase):

    def test_services_url_is_resolved(self):
        url = reverse('services')
        print(resolve(url))
        self.assertEquals(resolve(url).func, services)

    def test_services_detail_url_is_resolved(self):
        url = reverse('services_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, services_detail)

    def test_add_services_url_is_resolved(self):
        url = reverse('add_services')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_services)

    def test_edit_services_url_is_resolved(self):
        url = reverse('edit_services', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_services)

    def test_delete_services_url_is_resolved(self):
        url = reverse('delete_services', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_services)
