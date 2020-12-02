from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from .models import Task
from datetime import date
# Create your views here.

def index(request):
    todos = Task.objects.all() #On récupère tous les todos

    if request.method == "POST":
        if "addTask" in request.POST:
            content = request.POST["inputTaskContent"]
            is_done = False
            created_date = date.today()
            Todo = Task(content=content, is_done=is_done, created_date=created_date)
            Todo.save()
            return redirect("/todo")

    return render(request, 'todo/index.html',{"todos":todos})
