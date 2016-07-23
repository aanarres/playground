from django.shortcuts import render
from django.http import HttpResponse

# main view
def index(request):
    return HttpResponse("Hello, world. You're at the edu index.")
