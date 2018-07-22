# 默认返回参数
def resConfig(obj):
	def wrapper(*argv):
		obj.res_data = {
			'code': 1,
			'data': None,
			'msg': '未知错误'
		}
		return obj;
	return wrapper;