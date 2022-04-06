"""e2stem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView

from core import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('about/', TemplateView.as_view(template_name='about.html'), name="about"),        
    path('about/<str:language>/', TemplateView.as_view(template_name='about.html'), name="about"),        

    path('survey/', views.survey, name="survey"),         
    path('survey/<str:language>/', views.survey, name="survey"),  

    path('menstruation/', TemplateView.as_view(template_name='menstruation.html'), name="menstruation"),               
    path('menstruation/<str:language>/', TemplateView.as_view(template_name='menstruation.html'), name="menstruation"),        
 
    path('sharing/', views.sharing, name="sharing"),        
    path('sharing/<str:language>/', views.sharing, name="sharing"),  
      
    path('post/<str:post_id>/', views.post, name="post"),  
    path('post/<str:post_id>/<str:language>/', views.post, name="post"),  
    
    path('', TemplateView.as_view(template_name='home.html'), name="home"),        
    path('<str:language>/', TemplateView.as_view(template_name='home.html'), name="home"),            

]
