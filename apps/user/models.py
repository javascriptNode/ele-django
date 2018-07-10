from django.db import models

class User(object):
	user_id = models.IntegerField(primary_key=True,db_column='FId')
	username = models.CharField( max_length= 20 )
	password = models.CharField( max_length= 20 )
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
		


