from django.contrib import admin

from .models import TeachersModel


class TeachersAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "subjects_taught", 'profile_picture')
    search_fields = ('email', 'first_name', "last_name", "subjects_taught")


admin.site.register(TeachersModel, TeachersAdmin)
