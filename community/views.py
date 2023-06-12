from django.shortcuts import render
from accounts.models import User

def community_page(request):
    users = User.objects.all()
    return render(request, 'community_page.html', {'users': users})
