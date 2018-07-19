from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.core import serializers
from django.views import View
from django.core.cache import cache

from .models import User
from utils import decorstor



# 注册
@decorstor.resConfig
class signUp(View):
	def get(self, request):
		res_data = self.res_data
		username = request.POST.get('username',0)
		password = request.POST.get('password',0)
		s_code = request.POST.get('s_code',0)
		session_code = request.session.get('s_code',0)
		# 判断
		if(not username):
			res_data['msg'] = '用户名不能为空'
			return JsonResponse(res_data)
		if(not password):
			res_data['msg'] = '密码不能为空'
			return JsonResponse(res_data)
		if(not s_code):
			res_data['msg'] = '验证码不能为空'
			return JsonResponse(res_data)
		if(not session_code):
			res_data['msg'] = '无法获取验证码信息'
			return JsonResponse(res_data)			
		if(s_code.lower() != session_code.lower()):
			res_data['msg'] = '验证码错误'
			return JsonResponse(res_data)
		# 创建用户
		try:
			User.objects.get(username=username)
			res_data['msg'] = '用户已存在'
		except User.DoesNotExist:
			db = User(username=username, password=password)
			db.save()
			res_data['code'] = 0
			res_data['msg'] = '创建用户成功'
		return JsonResponse(res_data)

# 登录
@decorstor.resConfig
class signIn(View):	
	def get(self, request):
		
		res_data = self.res_data
		username = request.GET.get('username',0)
		password = request.GET.get('password',0)
		try:	
			db = User.objects.get(username=username)
			if(db.password == password):
				1
		except User.DoesNotExist:
			res_data['msg'] = '该用户不存在'
		cache.set('a', 888, timeout=)
		return JsonResponse( self.res_data )
