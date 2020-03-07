# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class UserReg(models.Model):

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$')
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=10)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=10)
    referralcode = models.CharField(max_length=7)
    
            
    





