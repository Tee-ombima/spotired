from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'teaser', 'body', 'display_image', 'start_date', 'end_date', 'timezone']
