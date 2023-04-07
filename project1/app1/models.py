from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=100)
    coll = models.CharField(max_length=100)
    add = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
