from django.urls import path
from . import views

urlpatterns = [
     path('', views.blog, name='my_blog'),
]
