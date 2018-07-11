from django.shortcuts import render
from django.http import JsonResponse

from PIL import Image

def imageCode():
	img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
	img.show()	
	with open('code.png','wb') as f:
	img.save(f,format='png')
	return JsonResponse( {  } )