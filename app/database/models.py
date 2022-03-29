from django.db import models

# Student model

class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False)
    grade = models.IntegerField(null=False)    
    teacher = models.CharField(max_length=100) 
        
    responses = models.TextField(null=False)  
    
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.name

    class Meta:

       ordering = ['created_at']

# Blog model

class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    text = models.TextField()    
    
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.name

    class Meta:

       ordering = ['created_at']
