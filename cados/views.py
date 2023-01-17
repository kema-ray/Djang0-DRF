from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def endpoints(request):
        data = ['/advocates/', 'advocates/:username']
        return JsonResponse(data, safe=False)

def advocate_list(request):
        data = ['Dennis','Rachel','Betty']
        return JsonResponse(data, safe=False)

def advocate_detail(request, username):
        data = username
        return JsonResponse(data, safe=False)