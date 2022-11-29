from operator import truediv
from pdb import post_mortem
from pickle import TRUE
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class College(models.Model):
    name = models.CharField(max_length=100,null=False) 
    address = models.CharField(max_length=100)
    description=models.TextField(max_length=500,default="Some String")
    image =models.URLField(default=None,null=True)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
 
class Course(models.Model):
    Name = models.CharField(max_length=100,null=False)


    def __str__(self):
        return self.Name


class Review(models.Model):
    college = models.CharField(max_length=255,null=False)
    comment = models.TextField( max_length=10000,default="Some String")
    rating= models.FloatField(default=0)

    def __str__(self):
        return self.college
 
class Student(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)


    def __str__(self):
        return "%s %s" %(self.first_name,self.last_name)


    
    


 