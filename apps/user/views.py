from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers


def login(request):
	print(request.GET.get('name'))
	return JsonResponse( {'a':1} )
