from django.shortcuts import render

def todolist(request):
  return render(request, 'todolist.html')

def create(request):
  return render(request, 'new.html')