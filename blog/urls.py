from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog_home, name='blog_home'),

]
