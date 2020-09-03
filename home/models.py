from django.db import models
import datetime


DESIGN_CHOICES = (
    ('Interiors', 'INTERIORS'),
    ('Exteriors', 'EXTERIORS'),
)


class Home(models.Model):
    name = models.CharField(max_length=28, null=False, blank=False)
    image = models.ImageField(upload_to='media/', default=None)
    description = models.TextField(max_length=400, default=None)
    design = models.CharField(
        choices=DESIGN_CHOICES, max_length=9, default=None
        )
    added = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
