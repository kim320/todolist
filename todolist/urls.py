from django.contrib import admin
from django.urls import path
import todolistapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolistapp.views.todolist, name='todolist'),
    path('todolist/new', todolistapp.views.new, name='new'),
    path('todolist/create', todolistapp.views.create, name='create'),
]
