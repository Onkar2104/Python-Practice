from django.db import models

# Create your models here.

class student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class fan(models.Model):
    name = models.CharField(max_length=20)

class car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name