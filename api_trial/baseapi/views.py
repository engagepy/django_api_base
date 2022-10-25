from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocates
from .serializers import AdvocateSerializer

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocates(request):
    #data = ['Zora', 'Time', 'Flies']
    advocates = Advocates.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def advocate_details(request, username):
    data = username
    return Response(data)


