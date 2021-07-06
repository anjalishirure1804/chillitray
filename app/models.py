from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_title=models.CharField(max_length=200)
    task_desc=models.CharField(max_length=2000,null=True)
    task_pic=models.ImageField(upload_to='productmage',null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task_title

class HierarchyModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    parent=models.CharField(max_length=100,default="Null")

    def __str__(self):
        return self.title