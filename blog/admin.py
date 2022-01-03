from django.contrib import admin

from .models import Post

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     form = PostForm
#     fields = ['content']
admin.site.register(Post)

