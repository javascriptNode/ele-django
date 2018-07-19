from django.contrib import admin
from django.utils.html import format_html
from .models import User

# Register your models here.
# class adminUser(admin.ModelAdmin):
# 	list_display = ('user_id', 'username', 'password', 'size' )
# 	def 修改名字(self,obj):
# 		return format_html('<input type="text" value="{a}"/>',a=obj)
# 		make.short_description = 'Name'

admin.site.register(User)

# admin.site.register(Manufacturer)