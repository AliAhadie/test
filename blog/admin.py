from django.contrib import admin
from blog.models import Post


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display = ('title','status','created_date')
    search_fields=('title','content')
    
    
admin.site.register(Post,BlogAdmin)    