from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def about(request):
    email = request.GET.get('email')
    print(email)
    return render(request, 'about.html') 

def contact(request):
    ism = request.GET.get('name')
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    message = request.GET.get('message')
    print(ism)
    print(phone)
    print(email)
    print(message)
    return render(request, 'contact.html') 

def main(request):
    ism = request.GET.get('name')
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    message = request.GET.get('message')
    number = request.GET.get('number')
    print(ism)
    print(phone)
    print(email)
    print(message)
    print(number)
    return render(request, 'index.html') 

def service(request):
    email = request.GET.get('email')
    print(email)
    return render(request, 'service.html') 
