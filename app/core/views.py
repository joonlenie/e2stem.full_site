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

        #article.subtitle_en = article.text_en.split("\n")[0]
        #article.subtitle_kh = article.text_kh.split("\n")[0]

        article.since_created = (datetime.now().date() - article.created_at).days

        article.created_at = article.created_at.strftime("%d-%b-%y")

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
    
        context = {}

        return render(request, 'survey.html', context)

    if request.method == 'POST':
    
        print(request.POST.dict())   
        print(dir(request.POST))         
        context = {}

        return render(request, 'survey-success.html', context)

        
