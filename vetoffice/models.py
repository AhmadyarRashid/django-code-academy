from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

class Patient(models.Model):
    breed = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    DOG = 'DO'
    CAT = 'CA'
    BIRD = 'BI'
    REPTILE = 'RE'
    OTHER = 'OT'
  