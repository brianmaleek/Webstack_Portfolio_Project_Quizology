# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'quiz_app/home.html')

def about(request):
    return render(request, 'quiz_app/about.html')
