from django.contrib import messages
from enum import auto
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from flask import request
from django.contrib.auth import authenticate,login,logout
from book.models import Field
from django.db.models import Q
# Create your views here.



def add(request):
    if request.method=='POST':
        name_=request.POST['name']
        authorName_=request.POST['authorName']
        price_=request.POST['price']
        select_=request.POST['select']
        insert_data=Field.objects.create(Book_Name=name_,Author_Name=authorName_,Price=price_,Book_Type=select_)
        insert_data.save()
        print(name_)
        return redirect('/')
   

    return render (request,'add.html')


def register(request):
    if request.method=="POST":
        uname=request.POST['username']
        upass=request.POST['password2']
        user=User(username=uname,password=upass,is_staff=1)
        user.save()
        return redirect('/book/add/')
    else:
        f=UserCreationForm()
        content={}
        content['form']=f
        return render (request,'register.html',content)

def userlogin(request):
    if request.method=='POST':
        af=AuthenticationForm(request=request,data=request.POST)
        if af.is_valid():
            uname=af.cleaned_data['username']
            upass=af.cleaned_data['password']
            is_authenticate=authenticate(username=uname , password=upass)
            if is_authenticate:
                login(request,is_authenticate)
                return redirect('/book/add/')
                messages.success(request,'login success')
        else:
            messages.error(request,'login failed try again !!!')

    af=AuthenticationForm()
    content={'form':af}
    return render(request,'userlogin.html',content)


def alldata(request):
    data=Field.customManager.filter(Is_Deleted='n')
    content={'data':data}
    return render(request,'alldata.html',content)

def delete(request,tid):
    record_deleted=Field.customManager.filter(id=tid)
    record_deleted.update(Is_Deleted='y')
    return redirect('/')

def update(request,tid):
    if request.method=="POST":
        name_=request.POST['name']
        authorName_=request.POST['authorName']
        price_=request.POST['price']
        select_=request.POST['select']
        record_update=Field.customManager.filter(id=tid)
        record_update.update(Book_Name=name_,Author_Name=authorName_,Price=price_,Book_Type=select_)
        return redirect('/')
    else:   
        data=Field.customManager.get(id=tid)
        content={'data':data}
        return render(request,'update.html',content)

def refersh (request):
    data=Field.customManager.all()
    content={'data':data}
    return render(request,'alldata.html',content)

def priceLtoH(request):
    data=Field.customManager.filter(Is_Deleted='n').order_by('Price')
    content={"data":data}
    return render(request,'alldata.html',content)
def priceHtoL(request):
    data=Field.customManager.filter(Is_Deleted='n').order_by('-Price')
    content={"data":data}
    return render(request,'alldata.html',content)

def nameasc(request):
    data=Field.customManager.filter(Is_Deleted='n').order_by('Author_Name')
    content={"data":data}
    return render(request,'alldata.html',content)

def namedsc(request):
    data=Field.customManager.filter(Is_Deleted='n').order_by('-Author_Name')
    content={"data":data}
    return render(request,'alldata.html',content)

def reference(request):
    Q1= Q(Is_Deleted='n')
    Q2=Q(Book_Type='Reference')
    content={}
    data=Field.customManager.filter(Q1&Q2)
    content={'data':data}
    return render(request,'alldata.html',content)
def fiction(request):
    Q1= Q(Is_Deleted='n')
    Q2=Q(Book_Type='Fiction')
    content={}
    data=Field.customManager.filter(Q1&Q2)
    content={'data':data}
    return render(request,'alldata.html',content)

def edited(request):
    Q1= Q(Is_Deleted='n')
    Q2=Q(Book_Type='Edited')
    content={}
    data=Field.customManager.filter(Q1&Q2)
    content={'data':data}
    return render(request,'alldata.html',content)
    Non-Fiction

def nfiction(request):
    Q1= Q(Is_Deleted='n')
    Q2=Q(Book_Type='Non-Fiction')
    content={}
    data=Field.customManager.filter(Q1&Q2)
    content={'data':data}
    return render(request,'alldata.html',content)