from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def genre(request):
    return HttpResponse('<h1>Hello worl from genre</h1>')