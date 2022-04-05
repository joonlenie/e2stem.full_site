from django.contrib import admin

# Register your models here.

from database.models import Student, BlogPost

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    search_fields = ['name', 'teacher']
    
    ordering = ['-created_at']



@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):

    search_fields = ['author', 'title']
    
    ordering = ['-created_at']
