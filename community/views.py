from django.core.paginator import Paginator
from django.shortcuts import render
from accounts.models import User

def member_list(request):
    users = User.objects.all()
    paginator = Paginator(users, 20)  # Display 20 members per page
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)
    return render(request, 'community_page.html', {'members': members})
