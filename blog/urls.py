from django.contrib import admin
from django.urls import path,include
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_home,name='blog'),
    path('post-<int:pid>',blog_single,name='blog_single')

    
]
