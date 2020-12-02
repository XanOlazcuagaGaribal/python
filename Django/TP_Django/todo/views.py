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
            todo = Task(content=content, is_done=is_done, created_date=created_date)
            todo.save()
            return redirect("/todo")
        if "deleteTask" in request.POST:
            toDelete = request.POST["deleteTask"] 
            for todo_id in toDelete:
                todo = Task.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
            return redirect("/todo")
        if "todoDone" in request.POST:   
            return redirect("/todo")  
    return render(request, 'todo/index.html',{"todos":todos})

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    if request.method == 'POST':
        return redirect('/todo/')

