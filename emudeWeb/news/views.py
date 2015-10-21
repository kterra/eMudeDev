from django.shortcuts import render
from news.models import Article
# Create your views here.

def home(request):
    article_list = Article.objects.order_by('-views')[:10]
    context_dict = { 'articles': article_list }
    return render(request, 'home.html', context_dict)

def article(request, article_title_slug):
    context_dict = {}

    try:
        article = Article.objects.get(slug = article_title_slug)
        context_dict['article'] = article
    except Article.DoesNotExist:
        print("This article does not exist!")

    return render(request, 'article.html', context_dict)
