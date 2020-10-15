from django.contrib import admin
from .models import Slides, MainContent, Contact


class SlidesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'tel',
        'mob',
        'email',
    )


class MainAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
    )


admin.site.register(Slides, SlidesAdmin)
admin.site.register(MainContent, MainAdmin)
admin.site.register(Contact, ContactAdmin)
