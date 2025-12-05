from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    pass 

class Asset(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=128, null=True, blank=True)
    asset_class = models.CharField(max_length=20)
    exchange = models.CharField(max_length=20)
    status = models.CharField(max_length=20) #active/inactive
    tradeable=models.BooleanField(default=True)
     
