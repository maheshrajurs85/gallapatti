import http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("<h1>helloWorld!!!!!!!!!!!!!</h1>");
    return render(request,'index.html',{'name':'myhomeeaaae'} )