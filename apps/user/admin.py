from django.contrib import admin
from django.utils.html import format_html
from .models import User, UserInfo

admin.site.register(User)
admin.site.register(UserInfo)
