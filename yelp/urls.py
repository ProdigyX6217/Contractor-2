from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Yelp.views import index, BusinessSearch, BusinessMatch, BusinessReview, PhoneView 


urlpatterns = [
    path('', index, name='index'),
    path('businessSearch/', BusinessSearch, name='Search'),
    path('businessReview/', BusinessReview, name='Review'),
    path('businessMatch/', BusinessMatch, name='Match'),
    path('businessPhone/', PhoneView.as_view(), name='Phone'),

]