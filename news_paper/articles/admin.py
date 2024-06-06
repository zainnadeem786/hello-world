from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Article
admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
 list_display = [
 "title",
 "body",
 "author",
 ]