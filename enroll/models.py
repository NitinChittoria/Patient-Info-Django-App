from django import forms
from django.db import models
# from datetime import datetime,timezone

from django.forms import widgets


# Create your models here.
class User(models.Model):
    
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    gender=models.CharField(max_length=70)
    age=models.IntegerField()
    disease=models.CharField(max_length=70)
    doctor_name=models.CharField(max_length=70)
    doctor_fees=models.IntegerField(default=500)
    
