from django.shortcuts import render, HttpResponse

# Create your views here.


def root(request):
    return HttpResponse('users')