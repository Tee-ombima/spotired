from django.urls import path
from .views import create_blog

urlpatterns = [
    path('blog/create/', create_blog, name='create_blog'),
    # Other URL patterns
]
