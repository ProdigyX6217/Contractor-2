from django.urls import path

from api.views import BusinessList, BusinessDetail

urlpatterns = [
    path('Yelp/', BusinessList.as_view(), name='Yelp_list'),
    path('Yelp/<int:pk>', BusinessDetail.as_view(), name='Yelp_detail')
]
