from django.db import models


class Services(models.Model):
    class Meta:
        verbose_name_plural = 'Services'

    title = models.CharField(max_length=28, null=False, blank=False)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title
