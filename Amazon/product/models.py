from django.db import models

# Create your models here.
class Producttable(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return 'Product '+ self.name