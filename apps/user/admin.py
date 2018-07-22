from django.contrib import admin

from .models import User
# Register your models here.
class UserTable(admin.ModelAdmin):
	list_display = ['createtime','username','password']
	search_fields = ['username','username']
admin.site.register(User, UserTable)