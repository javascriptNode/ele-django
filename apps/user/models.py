from django.db import models

class User(models.Model):
	createtime = models.DateTimeField( u'创建时间', auto_now_add=True, null=True )
	time = models.DateTimeField(u'时间', null=True)
	username = models.CharField( u'账号', max_length=20 )
	password = models.CharField( u'密码', max_length=20 )
	def __str__(self):
		return self.username
		


