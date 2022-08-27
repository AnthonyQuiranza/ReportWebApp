from http.client import HTTPResponse
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def registro_cuenta(request):
    return render(request,'registro-cuenta.html')