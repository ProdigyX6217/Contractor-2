from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from Yelp.models import Business
from django.views.generic import ListView
from django.conf import settings
import requests
import json
import os


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the yelp index.")

def BusinessSearch(request):
    yelp_client = 'LS6f-xpVxlngO2qWn-j724FR0LJv8PztM4Xd9HDcOmj7k6RTxY_BVjIiPuZJ5tq4OMYK-qx9Ls-mAQ9-u6547gvHqEYopMA1MR31VUcooDHaPjsUDSsRabQ1oLtZXnYx'
    # os.getenv('YELP_API_KEY')
    headers = {'Authorization': 'Bearer %s' % yelp_client}

    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':'bookstore','location':'New York City'}

    req = requests.get(url, params=params, headers=headers)

    # proceed only if the status code is 200
    # print(f'The status code is {req.status_code}')

    # print("***EXPECTED OUTPUT:***")
    parsed = json.loads(req.text)
    # print("***EXPECTED OUTPUT TYPE:***", type(parsed))
    # fun = {"HAPPY":"FUNNY"}
    # return render(request, 'search_results.html', {'fun': fun})

    # print(parsed)
    businesses = parsed["businesses"]

    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("\n")
    


'''
url='https://api.yelp.com/v3/businesses/search/phone'
params = {'phone':'+14159083801'}


url='https://api.yelp.com/v3/businesses/matches'
id="E8RJkjfdcwgtyoPMjQ_Olg"
url=f'https://api.yelp.com/v3/businesses/{id}'


url=f'https://api.yelp.com/v3/businesses/{id}/reviews'
'''

