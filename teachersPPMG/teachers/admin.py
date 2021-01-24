from django.contrib import admin
from django.shortcuts import redirect

from .models import TeachersModel


class TeachersAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "subjects_taught")
    search_fields = ('email', 'first_name', "subjects_taught")


admin.site.register(TeachersModel, TeachersAdmin)
