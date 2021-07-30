from django import forms
from django.forms import widgets
# from django.utils.html import TRAILING_PUNCTUATION_CHARS
from django.shortcuts import render
from .models import User

class PatientRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','gender','age','disease','doctor_name','doctor_fees']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'disease':forms.TextInput(attrs={'class':'form-control'}),
            'doctor_name':forms.TextInput(attrs={'class':'form-control'}),
            'doctor_fees':forms.NumberInput(attrs={'class':'form-control'}),
            
        }

