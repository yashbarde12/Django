from django.db import models

# Create your models here.
# CraveBites/menu/models.py

class MenuItem(models.Model):
    SNACKS = 'Snacks'
    BEVERAGES = 'Beverages'
    SWEETS = 'Sweets'

    CATEGORY_CHOICES = [
        (SNACKS, 'Snacks'),
        (BEVERAGES, 'Beverages'),
        (SWEETS, 'Sweets'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.category}'
