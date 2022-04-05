import os
        
import markdown
from markdown.extensions import attr_list
from datetime import datetime

from django.shortcuts import render
from django.utils import timezone

from database.models import Student, BlogPost                

     
"""
  
def blog(request, language):

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

"""
  
def sharing(request, language):

    articles = BlogPost.objects.all()

    for article in articles:

        article.text_en = markdown.markdown(article.text_en, extensions=['attr_list'])
        article.text_kh = markdown.markdown(article.text_kh, extensions=['attr_list'])

        article.description_en = article.text_kh.split("\n")[0]
        article.description_en = article.text_kh.split("\n")[0]

        #article.since_created = (datetime.now()- article.created_at).total_seconds()

            
    context = {

        'articles': articles

    }

    return render(request, 'sharing.html', context)


def post(request, post_id, language):

    article = BlogPost.objects.filter(pk=post_id)[0]

    article.text_en = markdown.markdown(article.text_en, extensions=['attr_list'])
    article.text_kh = markdown.markdown(article.text_kh, extensions=['attr_list'])

    context = {

        'article': article

    }

    return render(request, 'blog_post.html', context)
        
def survey(request, language):

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

        
