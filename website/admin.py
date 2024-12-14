from django.contrib import admin
from website.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','subject','created_date')
    date_hierarchy = 'created_date'


admin.site.register(Contact,ContactAdmin)
