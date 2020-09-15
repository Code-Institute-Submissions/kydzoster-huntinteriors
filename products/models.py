from django.db import models


DESIGN_CHOICES = (
    ('Interiors', 'INTERIORS'),
    ('Exteriors', 'EXTERIORS'),
)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.CharField(
        choices=DESIGN_CHOICES, max_length=9, default=None
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
