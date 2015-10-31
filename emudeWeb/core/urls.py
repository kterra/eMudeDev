from core import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^login/', views.login, name="login"),
    url(r'^user_dashboard/', views.user_dashboard, name="user_dashboard"),
]
