from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estás en el polls index")

def detail(request, question_id):
    return HttpResponse("Estás viendo una pregunta %s." % question_id)


def results(request, question_id):
    response = "Estás viendo los resultados de una pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estás votando")
    
# Create your views here.
