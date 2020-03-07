from django.urls import path
from accounts.views import SignUpView

# Create your views here.

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

