from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the yelp index.")

