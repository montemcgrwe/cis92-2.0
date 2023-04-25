#from django.shortcuts import render  #not sure where this came from
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
