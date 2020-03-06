from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Yelp.views import index, BusinessSearch


urlpatterns = [
    path('', index, name='index'),
    path('businessesSearch/', BusinessSearch, name='Search'),

    # path('/businesses/search/phone', views.index, name='index'),
    # path('/businesses/{id}', views.index, name='index'),
    # path('/businesses/{id}/reviews', views.index, name='index'),

]