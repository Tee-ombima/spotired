from django.urls import path
from .views import create_blog
from . import views


app_name = 'blogs'

urlpatterns = [
    path('create/', views.create_blog, name='create_blog'),
    # Other URL patterns
]
