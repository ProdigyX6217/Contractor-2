from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from Yelp.models import Business
from django.views import View
# from YelpAPI import get_my_key
import requests
import json

# Define API Key, Define Headers
api_key='LS6f-xpVxlngO2qWn-j724FR0LJv8PztM4Xd9HDcOmj7k6RTxY_BVjIiPuZJ5tq4OMYK-qx9Ls-mAQ9-u6547gvHqEYopMA1MR31VUcooDHaPjsUDSsRabQ1oLtZXnYx'
headers = {'Authorization': 'Bearer %s' % api_key}

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Yelp index.")

def BusinessSearch(request):
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':'boba','location':'San Francisco'} 
    req = requests.get(url, params=params, headers=headers)

    parsed = json.loads(req.text)
    businesses = parsed["businesses"]

    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("ID:", business["id"])
        print("\n")

    return render(request, 'business_search.html', {'businesses': businesses})

def BusinessMatch(request):
    url = 'https://api.yelp.com/v3/businesses/matches'
    params = {'name':'Tea Hut', 'address1':'2815 California St', 'city': 'San Francisco', 'state':'CA', 'country':'US'}
    req = req = requests.get(url, params=params, headers=headers)

    parsed = json.loads(req.text)
    businesses = parsed["businesses"]

    return render(request, 'business_match.html', {'businesses': businesses})

def BusinessReview(request):
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':'boba','location':'San Francisco'}
    req = requests.get(url, params=params, headers=headers)

    parsed = json.loads(req.text)
    businesses = parsed["businesses"]

    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("\n")

        id = business["id"]
        url="https://api.yelp.com/v3/businesses/" + id + "/reviews"
        req = requests.get(url, headers=headers)
        parsed = json.loads(req.text)

        reviews = parsed["reviews"]
        print("--- Reviews ---")

        for review in reviews:
            print("User:", review["user"]["name"], "Rating:", review["rating"], "Review:", review["text"], "\n")

        return render(request, 'business_review.html', {'reviews': reviews})

class PhoneView(View):
    
    def get(self, request):

        url = 'https://api.yelp.com/v3/businesses/search/phone'
        params = {'phone':'+14159083801','locale':'en_US'}
        req = requests.get(url, params=params, headers=headers)

        parsed = json.loads(req.text)
        businesses = parsed["businesses"]

        for business in businesses:
            print("Name:", business["name"])
            print("Phone:", business["phone"])
            print("\n")

        return render(request, 'business_phone.html', {'businesses': businesses})