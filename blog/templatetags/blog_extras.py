from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe



register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author, curr_user):
  
  if not isinstance(author, user_model):
    return ""

  if curr_user == author:
    print(curr_user.email)
    return format_html('<strong>me</strong>')

  if author.first_name and author.last_name:
    name = escape(f"{author.first_name} {author.last_name}")
  else:
    name = escape(f"{author.username}")

  if author.email:
    email = author.email
    prefix = format_html('<a href="mailto:{}">', email)
    suffix = format_html('</a>')
  else:
    prefix, suffix = "", ""

  return format_html('{}{}{}', prefix, name, suffix)