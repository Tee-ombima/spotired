from django.shortcuts import render
from accounts.models import User

def community_page(request):
    registered_users = User.objects.all()
    return render(request, 'community_page.html', {'registered_users': registered_users})
