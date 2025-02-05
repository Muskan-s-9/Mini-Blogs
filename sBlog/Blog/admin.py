from django.contrib import admin
from . models import Post, Contact

# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','tittle','desc']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address','message']
