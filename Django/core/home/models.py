from django.db import models

# Create your models here.

class student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()


class product(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class fan(models.Model):
    name = models.CharField(max_length=20)