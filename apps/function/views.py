from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from PIL import Image
from utils import code

# 获取验证码
def imageCode(request):
	data, s_code = code.check_code()
	# print(request.session.get("s_code", 0))
	request.session["s_code"] = s_code
	request.session.set_expiry(200)
	if( data ):
		response = {
			'code': 0,
			'msg': '成功',
			'data': {
				'code': data,
				's_code': s_code,
			},
		}
	else:
		response = {
			'code': 1,
			'msg': '失败',
			'data': {}
		}
	res = JsonResponse( response );
	# res['Access-Control-Allow-Origin'] = '*'
	return res;
