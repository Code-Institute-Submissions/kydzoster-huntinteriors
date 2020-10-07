from django.db import models


DESIGN_CHOICES = (
    ('Interiors', 'INTERIORS'),
    ('Exteriors', 'EXTERIORS'),
)


class Img(models.Model):

    class Meta:
        verbose_name_plural = 'Images'

    category = models.CharField(
        choices=DESIGN_CHOICES, max_length=9, default=None
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
