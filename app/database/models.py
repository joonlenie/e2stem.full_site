from datetime import datetime

from django.db import models

# Student model

class Student(models.Model):

    name = models.CharField(max_length=100)
            
    responses = models.TextField(null=False)  
    
    created_at = models.DateField(default=datetime.now)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.name

    class Meta:

       ordering = ['created_at']
       
"""
       
# Question model

class Question(models.Model):

    question_type = models.CharField(max_length=100)

    question = models.TextField(null=False)  
    options = models.TextField(null=False)     
     
    created_at = models.DateField(default=datetime.now)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.question

    class Meta:

       ordering = ['created_at']
       
       
# Answer model

class Answer(models.Model):

    student = models.ForeignKey(Student)
    question = models.ForeignKey(Question)
    answer = models.TextField(null=False)     
    
    created_at = models.DateField(default=datetime.now)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.name

    class Meta:

       ordering = ['created_at']
       
"""                     

# Blog model

class BlogPost(models.Model):

    title_en = models.CharField(max_length=200)
    title_kh = models.CharField(max_length=200)

    subtitle_en = models.CharField(max_length=500)
    subtitle_kh = models.CharField(max_length=500)

    text_en = models.TextField()  
    text_kh = models.TextField()    

    image = models.CharField(max_length=100)    
    author = models.CharField(max_length=100)  
    created_at = models.DateField(default=datetime.now)
    last_modified = models.DateField(auto_now=True)
    
    def __str__(self):

        return self.title_en

    class Meta:

       ordering = ['created_at']
