from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Yelp.views import index, BusinessSearch, BusinessReview


urlpatterns = [
    path('', index, name='index'),
    path('businessSearch/', BusinessSearch, name='Search'),
    path('businessReview/', BusinessReview, name='Review'),
    # path('/businesses/{id}/reviews', views.index, name='index'),

]