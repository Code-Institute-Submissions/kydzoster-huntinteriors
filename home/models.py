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

    def __str__(self):
        return self.title


class SubContent(models.Model):
    class Meta:
        verbose_name_plural = 'Sub Content'

    title = models.CharField(max_length=28, null=False, blank=False)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title
