from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from news.models import Article

# Register your models here.
class ArticleAdmin(MarkdownModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Article, ArticleAdmin)
