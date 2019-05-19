from django.shortcuts import render, get_object_or_404 , redirect
from django.utils import timezone
from .models import Todolist
import datetime

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
    if request.GET['due_date'] is '':
        todolist.due_date = None
    else:
        todolist.due_date = request.GET['due_date']
    todolist.level=request.GET['level']
    todolist.save()
    return redirect('/')

def edit(request, todolist_id):
    todolist = Todolist.objects.get(pk=todolist_id)
    if(request.method == 'POST'):
        todolist.title = request.POST['title']
        todolist.content = request.POST['content']
        if request.POST['due_date'] is '':
            todolist.due_date = None
        else:
            todolist.due_date = request.POST['due_date']
        todolist.level = request.POST['level']
        todolist.save()
        return redirect('/')

    return render(request, 'edit.html', {'todolist':todolist})

def destroy(request, todolist_id):
    todolist = Todolist.objects.get(pk=todolist_id)
    todolist.delete()
    return redirect('/')

def todolist_done(request, todolist_id):
    todolist = Todolist.objects.get(pk=todolist_id)
    todolist.done = True
    return redirect('/')