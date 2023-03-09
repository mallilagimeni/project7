from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ram(request):
    return HttpResponse('hero')

def sam(request):
    return HttpResponse('super man')
