from django.shortcuts import render
from django import forms
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404,redirect, render
from .models import *
from django.core.paginator import Paginator

from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.
def task(request):
    print("a")
    if request.method=="POST":
        task_title=request.POST['task_title']
        task_desc=request.POST['task_desc']
        task_pic=request.FILES['task_pic']
        ins=TaskModel(user=request.user,task_title=task_title,task_desc=task_desc,task_pic=task_pic)
        ins.save()

    return render(request,'app/task.html')
def viewtask(request):
    viewtask=TaskModel.objects.all()
    
    
    return render(request,'app/viewtask.html',{'viewtask':viewtask})

class SignUpView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/signup.html',{'form':form})
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!!,Your Account Has Been Registered Successfully')
            form.save()
        return render(request,'app/signup.html',{'form':form})

def hierarchy(request):
    print("a")
    if request.method=="POST":
        title=request.POST['title']
        parent=request.POST['parent']
        ins=HierarchyModel(user=request.user,title=title,parent=parent)

        ins.save()
    hierarchy=HierarchyModel.objects.all()
    context={'hierarchy':hierarchy}

    return render(request,'app/hierarchy.html',context)
   
    
def showhierarchy(request):
    hierarchy=HierarchyModel.objects.all()
    print(hierarchy)
    max=0
    s=""
    for x in hierarchy:
        # print(x.id)
        max+=1
    
    for x in hierarchy:
        if x.parent=="Null":
            # print("-"+x.title,end="\n")  
            s+="-"+x.title
            s+="\n"      
        else:
            x.parent=int(x.parent)
            # print(" "*x.parent+"-" +x.title,end="\n")
            s+=" "*x.parent+"-" +x.title
            s+="\n"
    
    print(s)
    
    return render(request,'app/showhierarchy.html')
   

 
    