from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers

def signUp(request):
	username = request.POST.get('username',0)
	password = request.POST.get('password',0)
	return JsonResponse({})

def signIn(request):
	username = request.POST.get('username',0)
	password = request.POST.get('password',0)
	
	# res = { 'code':  }
	return JsonResponse( {} )


