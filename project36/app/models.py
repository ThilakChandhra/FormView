from django.db import models

# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField(primary_key=True)
    saddress=models.TextField(max_length=200)
    squalification=models.CharField(max_length=10)

    def __str__(self):
        return self.sname
    