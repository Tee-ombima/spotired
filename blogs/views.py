from django.shortcuts import render, redirect
from .forms import BlogForm

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('/', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blogs/create_blog.html', {'form': form})
