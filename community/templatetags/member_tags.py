# member_tags.py
from django import template
from accounts.models import User

register = template.Library()

@register.simple_tag
def get_member_emails():
    users = User.objects.all()
    emails = [user.email for user in users]
    return emails

