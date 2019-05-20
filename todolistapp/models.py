from django.db import models
from django.utils import timezone
import datetime

class Todolist(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    due_date = models.DateField(blank=True, null=True)
    level = models.CharField(max_length=3, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def overdue(self):
        if self.due_date and datetime.date.today() > self.due_date:
            return True