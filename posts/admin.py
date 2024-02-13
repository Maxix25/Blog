from django.contrib import admin
from .models import Posts, Comment

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, PostsAdmin)
admin.site.register(Comment, CommentAdmin)