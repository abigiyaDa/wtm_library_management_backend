from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def author_view(request):
    title = 'new title'
    return render(request,'author.html', {'title':title})