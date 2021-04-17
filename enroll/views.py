
from django.shortcuts import render
from .forms import UserRegistration
from .models import User
from django.http import HttpResponseRedirect

########### Add data into Data base ################
def addData(request):
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            regi= User (name=name,email=email,password=password)
            regi.save()
            form=UserRegistration()
            

    else:
        form=UserRegistration()
    st=User.objects.all()
    return render(request,'enroll/addandupdate.html',{'form':form,'stu':st})


########### Delete Data From database #################

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete ()
        return HttpResponseRedirect('/')


######### Updata and delete Data ##########33

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi=User.objects.get(pk=id)
        fm=UserRegistration(instance=pi)
    return render(request,'enroll/updateUser.html',{'form':fm})


