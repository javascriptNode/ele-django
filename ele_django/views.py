from django.shortcuts import render
from django.http import HttpResponse, Http404

from django_redis import get_redis_connection
conn = get_redis_connection("default")

def index(request):
	return render(request,'index.html')