from django.contrib import admin
from django.urls import path
import todolistapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolistapp.views.todolist, name='todolist'),
    path('new',todolistapp.views.create, name='new'),
]
