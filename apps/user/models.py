from django.db import models
import ast


class ListField(models.TextField):
    # __metaclass__ = models.SubfieldBase
    description = "Stores a python list"
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    def to_python(self, value):
        if not value:
            value = []
 
        if isinstance(value, list):
            return value
 
        return ast.literal_eval(value)
 
    def get_prep_value(self, value):
        if value is None:
            return value
 
        return str(value)
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class UserInfo(models.Model):
	name = models.CharField( verbose_name=u'姓名', max_length=10 )
	age = models.IntegerField( verbose_name=U'年龄')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = '用户详情'

class User(models.Model):
	createtime = models.DateTimeField( verbose_name=u'创建时间', auto_now_add=True, null=True )
	username = models.CharField( verbose_name=u'账号', max_length=12, unique=True, null=True )
	password = models.CharField( verbose_name=u'密码', max_length=12, null=True )
	list = ListField( verbose_name=u'选择', null=True )
	select = models.OneToOneField( UserInfo, verbose_name=u'选择', on_delete=models.CASCADE, null=True )
	def __str__(self):
		return self.username
	class Meta:
		verbose_name_plural = "我的用户"
	
		

