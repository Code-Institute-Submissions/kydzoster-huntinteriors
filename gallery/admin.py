from django.contrib import admin
from .models import Img, Category


class ImgAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Img, ImgAdmin)
admin.site.register(Category, CategoryAdmin)
