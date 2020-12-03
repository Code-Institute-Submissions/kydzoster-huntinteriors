from django.test import TestCase
from django.urls import reverse, resolve
from home.views import index, manage, contact_form, title_detail,\
    slides_detail, add_slides, edit_slides, edit_title, delete_slides


class TestUrls(TestCase):

    def test_index_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_manage_url_is_resolved(self):
        url = reverse('manage')
        print(resolve(url))
        self.assertEquals(resolve(url).func, manage)

    def test_contact_form_url_is_resolved(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact_form)

    def test_title_detail_url_is_resolved(self):
        url = reverse('title_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, title_detail)

    def test_slides_detail_url_is_resolved(self):
        url = reverse('slides_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, slides_detail)

    def test_add_slides_url_is_resolved(self):
        url = reverse('add_slides')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_slides)

    def test_edit_slides_url_is_resolved(self):
        url = reverse('edit_slides', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_slides)

    def test_edit_title_url_is_resolved(self):
        url = reverse('edit_title', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_title)

    def test_delete_slides_url_is_resolved(self):
        url = reverse('delete_slides', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_slides)
