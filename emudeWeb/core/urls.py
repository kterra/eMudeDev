from core import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^login/', views.login, name="login"),
]
