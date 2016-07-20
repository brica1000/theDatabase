from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.blog_home, name='blog_home'),
    url(r'^my_beliefs/', views.my_beliefs, name='my_beliefs'),
    url(r'^update/', views.edit_beliefs, name='edit_beliefs'),
    url(r'^cs_scrape/', views.cs_scrape, name='cs_scrape'),

]
