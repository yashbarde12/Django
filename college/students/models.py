from django.db import models

# Create your models here.
# students/models.py

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    age = models.IntegerField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return self.name
