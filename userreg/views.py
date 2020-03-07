# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import UserReg
import random
import string

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'register.html')

def r_code(n=7):
        ref_code=string.ascii_letters + string.digits
        return (''.join(random.choice(ref_code) for i in range(n)))
mapping = dict()

def register(request):
    global u 
    global r 
    post = UserReg()
    post.username=request.POST.get('username')
    post.email=request.POST.get('email')
    post.age=request.POST.get('age')
    post.city=request.POST.get('city')
    post.referralcode=request.POST.get('referralcode')
    u = post.username
    r = post.referralcode
    
    if len(post.username)<1:
        messages.error(request,'enter the username')
    elif len(post.email)<1:
        messages.error(request,'enter the email')
    elif len(post.age)<1:
        messages.error(request,'enter the age')
    elif len(post.city)<1:
        messages.error(request,'enter the city')
    elif  len(post.referralcode)<1 :
        post.referralcode = r_code()
        post.save()
        mapping[post.username]=post.referralcode
    else:
        post.save()
        mapping[post.username]=post.referralcode
       
        
    return render(request,'register.html')


def output(request):
    table = UserReg.objects.all()
    args = {'table':table}
    return render(request,'output.html',args)
def mapp(request):
    return render(request,'map.html',{'mapping':mapping})
def find(request):
    ref = dict()
    for ke,value in mapping.items():
        if value == r:
            ref= {u:k for k,j in mapping.items() if j==value } 
    return render(request,'find.html',{'ref':ref})
    
    
