from django.contrib import admin

from .models import Technologies

@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    pass