from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# from yelp.models import Business
from django.conf import settings
import os
import requests
import json
# from dotenv import load_dotenv
# load_dotenv()

API_KEY="LS6f-xpVxlngO2qWn-j724FR0LJv8PztM4Xd9HDcOmj7k6RTxY_BVjIiPuZJ5tq4OMYK-qx9Ls-mAQ9-u6547gvHqEYopMA1MR31VUcooDHaPjsUDSsRabQ1oLtZXnYx"

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the yelp index.")

def BusinessSearch(request):
    yelp_client = API_KEY
    headers = {'Authorization': 'Bearer %s' % yelp_client}

    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':'bookstore','location':'New York City'}

    req = requests.get(url=url, params=params, headers=headers)

    print("***EXPECTED OUTPUT:***")
    parsed = json.loads(req.text)
    print("***EXPECTED OUTPUT TYPE:***", type(parsed))
    fun = {"HAPPY":"FUNNY"}
    return render('search_results.html', {'fun': fun})

    # businesses = parsed["businesses"]

    # for business in businesses:
    #     print("Name:", business["name"])
    #     print("Rating:", business["rating"])
    #     print("Address:", " ".join(business["location"]["display_address"]))
    #     print("Phone:", business["phone"])
    #     print("\n")
        

    # proceed only if the status code is 200
    # print(f'The status code is {req.status_code}')

    