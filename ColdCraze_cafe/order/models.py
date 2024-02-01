from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
   SNACKS = (('Burger','BURGER'),('Pizza','PIZZA'),('French fries','FRENCH FRIES'),('Sandwich','SANDWICH'))
   snacks = models.CharField(max_length=50, choices=SNACKS , blank=True, null=True)
   snack_quantity = models.IntegerField(blank=True, null=True)

   DRINKS = (('Chocolate Milkshake','CHOCOLATE MILKSHAKE'),('Mango Milkshake','MANGO MILKSHAKE'),
             ('Coffee','COFFEE'),('Sprite','SPRITE'),('Latte','LATTE'))
   drinks = models.CharField(max_length=50, choices=DRINKS, blank=True, null=True)
   drink_quantity = models.IntegerField(blank=True, null=True)

   DESERTS = (('Hot Chocolate','HOT CHOCOLATE'),('Belgian Waffle','BELGIAN WAFFLE'),
             ('Donuts','DONUTS'),('Cake','CAKE'),('Icecream','ICECREAM'))
   deserts = models.CharField(max_length=50, choices=DESERTS, blank=True, null=True)
   desert_quantity = models.IntegerField(blank=True, null=True)

   
   def __str__(self) :
      return "Order" 