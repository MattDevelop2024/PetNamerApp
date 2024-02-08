from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is an AI that will identify an animal in an unploaded picture. We will even suggest you names for it!")
