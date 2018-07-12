from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from PIL import Image
from util import check_code

def imageCode():
	data, s_code = check_code()
	HttpResponse(data, content_type='application/octet-stream');