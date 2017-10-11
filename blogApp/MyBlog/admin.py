from django.contrib import admin

# Register your models here.

from .models import *

class Post_admin(admin.ModelAdmin):
	admin.site.register(Post,)

class Comment_admin(admin.ModelAdmin):
	admin.site.register(Comment,)


