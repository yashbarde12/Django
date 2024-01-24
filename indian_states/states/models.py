from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)

    def __str__(self):
        return self.name
