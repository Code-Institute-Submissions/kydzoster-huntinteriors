from django.db import models


DESIGN_CHOICES = (
    ('Interiors', 'INTERIORS'),
    ('Exteriors', 'EXTERIORS'),
)


class Gallery(models.Model):

    class Meta:
        verbose_name_plural = 'Gallery'

    name = models.CharField(max_length=28, null=False, blank=False)
    image = models.ImageField(upload_to='media/gallery/', default=None)
    design = models.CharField(
        choices=DESIGN_CHOICES, max_length=9, default=None
        )
    description = models.TextField()

    def __str__(self):
        return self.name
