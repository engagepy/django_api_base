from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocates, Company
from .serializers import AdvocateSerializer, CompanySerializer
from django.db.models import Q
from rest_framework.views import APIView

# Create your views here.

# GET /advocates
# POST /advocates
# GET /advocates/:id
# PUT /advocates/:id
# DELETE /advocates/:id



@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username', '/company']
    return Response(data)

@api_view(['GET', 'POST'])
def advocates(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocate = Advocates.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        #data = ['Zora', 'Time', 'Flies']
        serializer = AdvocateSerializer(advocate, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        advocate = Advocates.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)


class AdvocateDetails(APIView):

    def get_object(self,username):
        try:
            return Advocates.objects.get(username=username)
        except ValueError as e:
            raise e

    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        advocate = self.get_object(username)

        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('Entry Deleted')
        
# Function Based CRUD View

# @api_view(['GET','PUT','DELETE'])
# def advocate_details(request, username):
#     advocate = Advocates.objects.get(username=username)

#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']

#         advocate.save()

#         serializer = AdvocateSerializer(advocate, many=False)

#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('Entry Deleted')



@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)
