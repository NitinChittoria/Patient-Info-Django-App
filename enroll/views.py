from .models import User
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render,HttpResponseRedirect
from .forms import PatientRegistration

# Create your views here.
def create_user(request):
    if request.method=='POST':
        pr=PatientRegistration(request.POST)
        if pr.is_valid():
            fn=pr.cleaned_data['first_name']
            ln=pr.cleaned_data['last_name']
            g=pr.cleaned_data['gender']
            a=pr.cleaned_data['age']
            d=pr.cleaned_data['disease']
            dn=pr.cleaned_data['doctor_name']
            df=pr.cleaned_data['doctor_fees']
            # d=pr.cleaned_data['date']
            reg=User(first_name=fn,last_name=ln,gender=g,age=a,disease=d,doctor_name=dn,doctor_fees=df)
            reg.save()
            pr=PatientRegistration()

    
    else:
        pr=PatientRegistration()
    patient=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':pr,'pat':patient})


#this function will delete patient info
def delete_data (request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


#this function will update patient info
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pr=PatientRegistration(request.POST,instance=pi)
        if pr.is_valid():
            pr.save()
    else:
        pi=User.objects.get(pk=id)
        pr=PatientRegistration(instance=pi)

    return render(request,'enroll/updatedata.html',{'form':pr})