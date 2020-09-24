from django.contrib import admin
from .models import Testament


class TestamentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'date',
    )


admin.site.register(Testament, TestamentAdmin)
