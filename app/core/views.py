from django.shortcuts import render

from database.models import Student                

import os
        
import markdown
from markdown.extensions import attr_list
      
  
def blog(request):

    markdown_dir = 'blog'

    articles = []

    for directory in os.listdir(markdown_dir):

        en_markdown_path = "{}/{}/en.md".format(markdown_dir, directory)
        kh_markdown_path = "{}/{}/kh.md".format(markdown_dir, directory)

        en_markdown = open(en_markdown_path, 'r').read()
        kh_markdown = open(kh_markdown_path, 'r').read()

        en_html = markdown.markdown(en_markdown, extensions=['attr_list'])
        kh_html = markdown.markdown(kh_markdown, extensions=['attr_list'])

        article = {

          'en': en_html,
          'kh': kh_html

        }

        articles.append(article)
                    
    context = {

        'articles': articles

    }

    return render(request, 'blog.html', context)

        
def survey(request):

    if request.method == 'GET':
    
        students = Student.objects.all()
        
        student_count = len(students)
        
        context = {
        
          'student_count': student_count
          
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
        print(question_one)
        
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

        
