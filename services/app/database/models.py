# Create models to 

from django.db import models

# Teacher model

class Teacher(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)    
    
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.name

    class Meta:

       ordering = ['created_at']
       
       
# Student model

class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.name

    class Meta:

       ordering = ['created_at']
