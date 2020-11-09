from django.contrib import admin
from .models import Slides, MainContent


class SlidesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
    )


class MainAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


admin.site.register(Slides, SlidesAdmin)
admin.site.register(MainContent, MainAdmin)
