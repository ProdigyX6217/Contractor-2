from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from Yelp.models import Business
from api.serializers import BusinessSerializer

# Create your views here.
class BusinessList(APIView):
    def get(self, request):
        businesses = Business.objects.all()[:20]
        data = BusinessSerializer(businesses, many=True).data
        return Response(data)

class BusinessDetail(APIView):
    def get(self, request, pk):
        business = get_object_or_404(Business, pk=pk)
        data = BusinessSerializer(business).data
        return Response(data)


