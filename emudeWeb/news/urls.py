from django.conf.urls import include, url
from news import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/(?P<article_title_slug>[\w\-]+)/$', views.article, name='article')
]
