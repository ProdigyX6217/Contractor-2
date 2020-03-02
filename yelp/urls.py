from django.urls import path
from yelp import views

app_name = 'yelp'

api_key='LS6f-xpVxlngO2qWn-j724FR0LJv8PztM4Xd9HDcOmj7k6RTxY_BVjIiPuZJ5tq4OMYK-qx9Ls-mAQ9-u6547gvHqEYopMA1MR31VUcooDHaPjsUDSsRabQ1oLtZXnYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'
url='https://api.yelp.com/v3/businesses/search/phone'
url='https://api.yelp.com/v3/businesses/matches'


urlpatterns = [
    path('', views.index, name='index'),
    path('/businesses/search', views.index, name='index'),
    path('/businesses/search/phone', views.index, name='index'),
    path('/businesses/{id}', views.index, name='index'),
    path('/businesses/{id}/reviews', views.index, name='index'),

]