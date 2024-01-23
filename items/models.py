from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=400)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description[0:30]
