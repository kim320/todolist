from django.shortcuts import render, get_object_or_404 , redirect
from django.utils import timezone
from .models import Todolist

def todolist(request):
    today = timezone.datetime.now()
    todolists = Todolist.objects
    return render(request, 'todolist.html', {'todolists':todolists, 'today':today})

def new(request):
    return render(request, 'new.html')

def create(request):
    todolist = Todolist()
    todolist.title = request.GET['title']
    todolist.content = request.GET['content']

    todolist.save()
    return redirect('/')

def edit(request, todolist_id):
    todolist = Todolist.objects.get(pk=todolist_id)
    return render(request, 'edit.html', {'todolist':todolist})

def update(request, todolist_id):
    todolist = Todolist.objects.get(pk=todolist_id)
    todolist.title = request.GET['title']
    todolist.content = request.GET['content']
    todolist.save()
    return redirect('/')

def destroy(request, todolist_id):
    todolist = Todolist.objects.get(pk=todolist_id)
    todolist.delete()
    return redirect('/')