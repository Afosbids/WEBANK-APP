from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>weBank Project Setup, Docker works fine :-)  </h1>")

# Create your views here.
