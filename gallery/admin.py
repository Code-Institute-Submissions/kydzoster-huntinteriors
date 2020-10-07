from django.contrib import admin
from .models import Img


class ImgAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'image',
    )

    ordering = ('category',)


admin.site.register(Img, ImgAdmin)
