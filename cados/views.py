from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def endpoints(request):
        data = ['/advocates/', 'advocates/:username']
        return Response(data)
        # return JsonResponse(data, safe=False)

@api_view(['GET'])
def advocate_list(request):
        query = request.GET.get('query')

        if query == None:
                query = ''

        advocates = Advocate.objects.filter(Q(username__icontains = query) | Q(bio__icontains = query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
        # return JsonResponse(data, safe=False)

@api_view(['GET'])
def advocate_detail(request, username):
        # data = username
        advocate = Advocate.objects.get(username=username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
        # return JsonResponse(data, safe=False)