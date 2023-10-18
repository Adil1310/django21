from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title