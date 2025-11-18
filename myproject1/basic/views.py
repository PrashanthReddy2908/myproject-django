from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def sample(request):
    return HttpResponse("hello world")
def sample1(request):
    return HttpResponse("welcome to Django")
def sampleinfo(request):
    # data={"name":"prashu","age":24,"city":"hyd"}
    data={'result':[4,5,6,6,7]}
    return JsonResponse(data)

def dynamicResponse(request):
    name=request.GET.get("name",'')
    city=request.GET.get("city",'')
    return HttpResponse(f"Hello {name} from {city}")

def info(request):
    name=request.GET.get("name","")
    address=request.GET.get("address","")
    age=request.GET.get("age","")
    return HttpResponse(f"{name} from {address} and {age} years old")