from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def book(request):
    return HttpResponse('<h1>hello from book</h1>')
