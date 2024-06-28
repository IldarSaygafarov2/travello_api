from django.shortcuts import render, HttpResponse

# Create your views here.


def root(request):
    return HttpResponse('users')


# /login
# /registation
# /code/send
# /code/check
# /reset/phone
# /reset/email
# /reset/password
