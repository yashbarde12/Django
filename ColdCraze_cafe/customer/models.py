from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20, null=False)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=100)