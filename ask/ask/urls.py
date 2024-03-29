"""ask URL Configuration

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
from django.urls import re_path

admin.autodiscover()

from qa import views

urlpatterns = [
    #path(r'^login/', include('qa.urls')),
    #path(r'^$', include('qa.urls')),                                                              
    #path(r'^login/.*$', include('qa.urls')),                                    
    #path(r'^signup/.*', include('qa.urls')),                                   
    #path(r'^question/(?P<id>[0-9]+)/$', include('qa.urls')),                 
    #path(r'^ask/.*',  include('qa.urls')),                                         
    #path(r'^popular/.*', include('qa.urls')),                                 
    #path(r'^new/.*', include('qa.urls')),
    path('^$', views.test),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    #path('question/<[0-9]+>/', views.test, name='question'),
    #path('question/<int:id>/', views.test, name='question'),
    re_path(r'^question/<\d+>/', views.test, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new'),
]
