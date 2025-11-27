from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=100)
    sid=models.IntegerField()
    sage = models.IntegerField()
    
    def __str__(self):
        return self.sname