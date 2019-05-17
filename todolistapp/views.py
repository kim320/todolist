from django.shortcuts import render, get_object_or_404 , redirect
from .models import Todolist

def todolist(request):
    todolists = Todolist.objects
    return render(request, 'todolist.html', {'todolists':todolists})

def new(request):
    return render(request, 'new.html')

def create(request):
    todolist = Todolist()
    todolist.title = request.GET['title']
    todolist.content = request.GET['content']

    todolist.save()
    return redirect('/')