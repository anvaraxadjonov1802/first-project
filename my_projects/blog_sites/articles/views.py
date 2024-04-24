from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('<h1>Hello world!</h1>')

def secound(request):
    return HttpResponse('<h1>Salom dunyo!</h1>')


