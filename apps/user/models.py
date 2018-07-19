from django.db import models
from django.utils.html import format_html
from django.conf import settings

# class Manufacturer(models.Model):
#     name = models.CharField(verbose_name=u'我的名字', max_length=5, null=True)
#     age = models.TimeField(verbose_name=u'我的世界', null=True)
#     def __str__(self):
#     	return self.name

class User(models.Model):
	createtime = models.DateTimeField( verbose_name=u'创建时间', auto_now_add=True, null=True )
	username = models.CharField( verbose_name=u'账号', max_length=20, unique=True, null=True )
	password = models.CharField( verbose_name=u'密码', max_length=20, null=True )
	def __str__(self):
		return self.username
	class Meta:
		verbose_name = '前端用户'
	
		

