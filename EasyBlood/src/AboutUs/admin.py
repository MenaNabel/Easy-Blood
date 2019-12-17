from django.contrib import admin
from .models import AboutUs
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_filter = ['active' , 'created']
    list_display = ['title' , 'user' , 'active']
    search_fields = ['title']

admin.site.register(AboutUs , PostAdmin)