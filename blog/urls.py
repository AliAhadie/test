from django.contrib import admin
from django.urls import path,include
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_home,name='blog'),
    path('blog-single/',blog_single,name='blog_single')

    
]
