from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'description',
        'design',
    )

    ordering = ('name',)


admin.site.register(Gallery, GalleryAdmin)
