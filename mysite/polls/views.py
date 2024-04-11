from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estás en el polls index")
    
# Create your views here.
