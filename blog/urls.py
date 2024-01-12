from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('category/<slug:category_slug>', category, name='category'),
    path('articles', articles, name='articles'),
    path('detail/<slug:slug>', detail, name='detail')
]