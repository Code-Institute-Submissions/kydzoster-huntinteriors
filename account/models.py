from django.db import models
from django.conf import settings


class Profile(models.Model):
    # when user is deleted, its profile is also deleted
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%d/%m/%Y/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
