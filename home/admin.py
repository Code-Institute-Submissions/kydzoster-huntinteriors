from django.contrib import admin
from .models import Slides, MainContent, SubContent, Contact


class SlidesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
    )


class SubContentAdmin(admin.ModelAdmin):
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


admin.site.register(Slides, SlidesAdmin)
admin.site.register(MainContent)
admin.site.register(SubContent, SubContentAdmin)
admin.site.register(Contact, ContactAdmin)
