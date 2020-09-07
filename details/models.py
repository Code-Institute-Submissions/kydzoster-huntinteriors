from django.db import models


DESIGN_CHOICES = (
    ('Interiors', 'INTERIORS'),
    ('Exteriors', 'EXTERIORS'),
)


class Details(models.Model):

    class Meta:
        verbose_name_plural = 'Details'

    name = models.CharField(max_length=28, null=False, blank=False)
    image = models.ImageField(upload_to='media/details/', default=None)
    description = models.TextField()
    design = models.CharField(
        choices=DESIGN_CHOICES, max_length=9, default=None
        )

    def __str__(self):
        return self.name
