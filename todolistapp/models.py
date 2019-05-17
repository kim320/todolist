from django.db import models
from django.utils import timezone

class Todolist(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title