from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student
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


# to test database connection
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"Status":"ok ","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})

@csrf_exempt
def addStudent(request):
    print(request.method)
    if request.method=="POST":
        data=json.loads(request.body)
        student=Student.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email')) 
        return JsonResponse({"status":"success","id":student.id},status=200)
    return JsonResponse({"error":"Use post method"},status=400)
