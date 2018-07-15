from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers

from user.models import User
# 注册
def signUp(request):
	response = {
		'code': 1,
		'data': None,
		'msg': '请求类型错误'
	}
	if(request.method == 'GET'):
		username = request.GET.get('username',0)
		password = request.GET.get('password',0)
		s_code = request.GET.get('s_code',0)
		session_code = request.session.get('s_code',0)
		# 判断
		if(not username):
			response['msg'] = '用户名不能为空'
			return JsonResponse(response)
		if(not password):
			response['msg'] = '密码不能为空'
			return JsonResponse(response)
		if(not s_code):
			response['msg'] = '验证码不能为空'
			return JsonResponse(response)
		if(not session_code):
			response['msg'] = '无法获取验证码信息'
			return JsonResponse(response)			
		if(s_code != session_code):
			response['msg'] = '验证码错误'
			return JsonResponse(response)
		# 创建	
		try:
			User.objects.get(username=username)
			response['msg'] = '用户已存在'
		except:
			db = User(username=username, password=password)
			db.save()
			response['code'] = 0
			response['msg'] = '创建用户成功'
	return JsonResponse(response)

# 登录
def signIn(request):
	username = request.POST.get('username',0)
	password = request.POST.get('password',0)
	
	# res = { 'code':  }
	return JsonResponse( {} )


