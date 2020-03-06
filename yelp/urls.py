from django.urls import path
from yelp.views import index, BusinessSearch
from django.conf import settings


app_name = 'yelp'


'''
url='https://api.yelp.com/v3/businesses/search/phone'

params = {'phone':'+14159083801'}


url='https://api.yelp.com/v3/businesses/matches'


id="E8RJkjfdcwgtyoPMjQ_Olg"
url=f'https://api.yelp.com/v3/businesses/{id}'


url=f'https://api.yelp.com/v3/businesses/{id}/reviews'
'''


urlpatterns = [
    path('', index, name='index'),
    path('businesses/search/', BusinessSearch, name='Search'),

    # path('/businesses/search/phone', views.index, name='index'),
    # path('/businesses/{id}', views.index, name='index'),
    # path('/businesses/{id}/reviews', views.index, name='index'),

]