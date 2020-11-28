from django.db import models
from django.conf import settings
from django_countries.fields import CountryField


class Profile(models.Model):
    # when user is deleted, its profile is also deleted
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%M/%d', blank=True)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=50)
    post_code = models.CharField(blank=True, max_length=8)
    country = CountryField(blank=True, max_length=50)

    def __str__(self):
        return f'Profile for user {self.user.username}'
