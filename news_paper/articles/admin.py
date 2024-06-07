from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Article
from .models import Article, Comment # new
class CommentInline(admin.TabularInline): # new: # new
 model = Comment
 extra = 0 # new
class ArticleAdmin(admin.ModelAdmin): # new
 inlines = [
 CommentInline,
 ]
 list_display = [
 "title",
 "body",
 "author",
 ]


class ArticleAdmin(admin.ModelAdmin):
 list_display = [
 "title",
 "body",
 "author",
 ]
admin.site.register(Comment) # new
admin.site.register(Article, ArticleAdmin) # new

