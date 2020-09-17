from django.contrib import admin
from .models import Slides, MainContent, SubContent


class SlidesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
    )


class MainContentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class SubContentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
    )


admin.site.register(Slides, SlidesAdmin)
admin.site.register(MainContent, MainContentAdmin)
admin.site.register(SubContent, SubContentAdmin)
