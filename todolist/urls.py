from django.contrib import admin
from django.urls import path
import todolistapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolistapp.views.todolist, name='todolist'),
    #path('todolist/todo', todolistapp.views.todo, name='todo'),
    #path('todolist/done', todolistapp.views.done, name='done'),
    path('todolist/new', todolistapp.views.new, name='new'),
    path('todolist/create', todolistapp.views.create, name='create'),
    path('todolist/destroy/<int:todolist_id>', todolistapp.views.destroy, name='destroy'),
    path('todolist/edit/<int:todolist_id>', todolistapp.views.edit, name='edit'),
    path('todolist/todolist_done/<int:todolist_id>', todolistapp.views.todolist_done, name='todolist_done'),
]
