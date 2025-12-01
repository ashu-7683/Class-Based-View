from django.db import models

# Create your models here.
class School(models.Model):
    scname = models.CharField(max_length=100)
    scloc = models.CharField(max_length=100)
    scprincipal = models.CharField(max_length=100)
    
    def __str__(self):
        return self.scname
    
class Student(models.Model):
    stname = models.CharField(max_length=100)
    stage = models.IntegerField()
    scname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')