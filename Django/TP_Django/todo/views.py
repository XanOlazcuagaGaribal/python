from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Task
# Create your views here.

def index(request):
    return render(request, 'todo/index.html')