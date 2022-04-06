import os
        
import markdown
from markdown.extensions import attr_list
from datetime import datetime

from django.shortcuts import render
from django.utils import timezone

from database.models import Student, BlogPost                

     

  
def sharing(request, language='en'):

    articles = BlogPost.objects.all()

    for article in articles:

        article.text_en = markdown.markdown(article.text_en, extensions=['attr_list'])
        article.text_kh = markdown.markdown(article.text_kh, extensions=['attr_list'])

        article.description_en = article.text_kh.split("\n")[0]
        article.description_en = article.text_kh.split("\n")[0]

        #article.since_created = (datetime.now()- article.created_at).total_seconds()

            
    context = {

        'articles': articles,
        'language': language
    }

    return render(request, 'sharing.html', context)


def post(request, post_id, language='en'):

    article = BlogPost.objects.filter(pk=post_id)[0]

    article.text_en = markdown.markdown(article.text_en, extensions=['attr_list'])
    article.text_kh = markdown.markdown(article.text_kh, extensions=['attr_list'])

    context = {

        'article': article,
        'language': language

    }

    return render(request, 'post.html', context)

        
def survey(request, language='en'):

    if request.method == 'GET':
    
        students = Student.objects.all()
        
        student_count = len(students)
        
        context = {
        
          'student_count': student_count,
          'language': language
          
        }

        return render(request, 'survey.html', context)

  
    if request.method == 'POST':
    
        # print(request.POST)   
         
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        teacher = request.POST.get('teacher')        
                
        question_one = request.POST.get('q-1')     
        question_two = request.POST.get('q-2')       
        
        responses = [question_one, question_two]
        responses_str = "\n\n".join(responses)
                                            
        student = Student(
        
          name=name, 
          age=int(age),
          grade=int(grade), 
          teacher=teacher, 
          responses=responses_str   
               
        )
        
        student.save()
        
        context = {}

        return render(request, 'survey.html', context)

        
