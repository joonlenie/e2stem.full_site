from django.contrib import admin

# Register your models here.

from database.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    search_fields = ['name', 'teacher']
    
    ordering = ['-created_at']

