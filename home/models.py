from django.db import models


class Slides(models.Model):
    class Meta:
        verbose_name_plural = 'Slides'

    title = models.CharField(max_length=28, null=False, blank=False)
    image = models.ImageField()

    def __str__(self):
        return self.title


class MainContent(models.Model):
    class Meta:
        verbose_name_plural = 'Title'

    title = models.CharField(max_length=28, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact'

    address = models.TextField(max_length=100, blank=True)
    tel = models.CharField(max_length=11, blank=True)
    mob = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=70, blank=True)

    def __str__(self):
        return self.email
