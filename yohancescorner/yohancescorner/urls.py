from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('yelp/', include('yelp.urls')),
    path('admin/', admin.site.urls),
]