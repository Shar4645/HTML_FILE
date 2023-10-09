from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title' : 'Home page',
        
    }