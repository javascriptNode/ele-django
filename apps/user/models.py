from django.db import models

class User(object):
	username = CharField( max_length= 20 )
	password = CharField( max_length= 20 )
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
		


