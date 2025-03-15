from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'created_at', 'updated_at')
    search_fields = ['name', 'email']
    list_filter = ('course',)
    ordering = ['name']

admin.site.register(Student, StudentAdmin)
