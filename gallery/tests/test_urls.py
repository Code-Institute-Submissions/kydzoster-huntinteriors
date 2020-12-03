from django.test import TestCase
from django.urls import reverse, resolve
from gallery.views import all_gallery, image_detail, add_image, edit_image,\
    delete_image


class TestUrls(TestCase):

    def test_all_gallery_url_is_resolved(self):
        url = reverse('gallery')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_gallery)

    def test_image_detail_url_is_resolved(self):
        url = reverse('image_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, image_detail)

    def test_add_image_url_is_resolved(self):
        url = reverse('add_image')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_image)

    def test_edit_image_url_is_resolved(self):
        url = reverse('edit_image', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_image)

    def test_delete_image_url_is_resolved(self):
        url = reverse('delete_image', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_image)
