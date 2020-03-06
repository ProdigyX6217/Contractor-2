from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# from yelp.models import Business
from django.conf import settings
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the yelp index.")

def BusinessSearch(request):
    yelp_client = os.getenv("API_KEY")
    headers = {'Authorization': 'Bearer %s' % yelp_client}

    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':'bookstore','location':'New York City'}

    req = requests.get(url, params=params, headers=headers)

    parsed = json.loads(req.text)
    print(parsed)

    # businesses = parsed["businesses"]

    # for business in businesses:
    #     print("Name:", business["name"])
    #     print("Rating:", business["rating"])
    #     print("Address:", " ".join(business["location"]["display_address"]))
    #     print("Phone:", business["phone"])
    #     print("\n")
        

    # proceed only if the status code is 200
    # print(f'The status code is {req.status_code}')

    