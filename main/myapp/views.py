from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("yaaa")

def index(request):
	return HttpResponse("preeettt")
