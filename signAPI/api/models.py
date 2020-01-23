from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class accounts(models.Model):
    Name=models.CharField(max_length=200,blank=False)
    Phone=PhoneNumberField()
    Email=models.EmailField(blank=False)
    username=models.CharField(max_length=100,blank=False)
    userid=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=200,blank=False)
    salt=models.CharField(max_length=300,blank=True)

class bio(models.Model):
    Name=models.CharField(max_length=200,blank=False)
    Phone=models.CharField(max_length=20)
    Email=models.EmailField(blank=False)