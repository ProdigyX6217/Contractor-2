from django.urls import path
from yelp import views
import requests
import json

app_name = 'yelp'


headers = {'Authorization': f'Bearer {api_key}'}


url='https://api.yelp.com/v3/businesses/search'

# In the params dictionary, term takes string values.
params = {'term':'seafood','location':'San Francisco'}

# Making a get request to the API.
req=requests.get(url, params=params, headers=headers)

# Convert the data into a JSON object.
parsed = json.loads(req.text)
 
# proceed only if the status code is 200
print(f'The status code is {req.status_code}')

'''
url='https://api.yelp.com/v3/businesses/search/phone'

params = {'phone':'+14159083801'}


url='https://api.yelp.com/v3/businesses/matches'


id="E8RJkjfdcwgtyoPMjQ_Olg"
url=f'https://api.yelp.com/v3/businesses/{id}'


url=f'https://api.yelp.com/v3/businesses/{id}/reviews'
'''


urlpatterns = [
    path('', views.index, name='index'),
    path('/businesses/search', views.index, name='index'),
    # path('/businesses/search/phone', views.index, name='index'),
    # path('/businesses/{id}', views.index, name='index'),
    # path('/businesses/{id}/reviews', views.index, name='index'),

]