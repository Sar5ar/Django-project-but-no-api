from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class ser(AbstractUser): 
    manzil=models.CharField(max_length=200,null=True,blank=True)
    rasmingiz=models.ImageField(upload_to='img',null=True,blank=True)
    def __str__(self):
        return self.username
    
class Tavarlar(models.Model):
    nomi=models.CharField(max_length=120)
    kim=models.CharField(max_length=120,null=True,blank=True)
    rasmi=models.ImageField(upload_to='img')
    narxi=models.DecimalField(max_digits=100000000,decimal_places=3,null=True,blank=True)
    kim_tamonidan=models.ForeignKey(ser,on_delete=models.CASCADE,null=True,blank=True)
    tanlash=models.BooleanField(null=True,blank=True)
    coment=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.nomi

class saqlash(models.Model):
    s_nomi=models.CharField(max_length=120,null=True,blank=True)
    s_rasmi=models.ImageField(upload_to='img',null=True,blank=True)
    narxi=models.DecimalField(max_digits=100000000,decimal_places=3,null=True,blank=True)
    kim=models.CharField(max_length=120,null=True,blank=True)

