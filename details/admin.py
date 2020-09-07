from django.contrib import admin
from .models import Details


class DetailsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'description',
        'design',
    )

    ordering = ('name',)


admin.site.register(Details, DetailsAdmin)
