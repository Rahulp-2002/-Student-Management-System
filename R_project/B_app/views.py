from django.shortcuts import render,redirect
from B_app.models import Students
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def my_page(request):
    data=Students.objects.all()
    return render(request, "MY_WEB_PAGE.html" ,{"display":data})

def add_page(request):
    if request.method =="POST":
        a=request.POST['name']
        b=request.POST['dob']
        c=request.POST['mobile']
        d=request.POST['email']
        e=request.POST['gender']
        data=Students(name=a,dob=b,mobile=c,email=d,gender=e)
        data.save()
        return redirect("/RP")
    return render(request, 'Add.html')

def edit_page(request,id):
    data=Students.objects.get(id=id)
    if request.method =="POST":
        a=request.POST['name']
        b=request.POST['dob']
        c=request.POST['mobile']
        d=request.POST['email']
        e=request.POST['gender']

        data.name=a
        data.dob=b
        data.mobile=c
        data.email=d
        data.gender=e
        data.save()
        return redirect("/RP")
    return render(request, 'Edit.html',{"show":data})

def details_page(request,id):
    data=Students.objects.get(id=id)
    return render(request, 'Details.html',{"info":data})

def delete_page(request,id):
    data=Students.objects.get(id=id)
    data.delete()
    return redirect("/RP")

def register_page(request):
    if request.method == 'POST':
        a=request.POST['name']
        b=request.POST['email']
        c=request.POST['pass1']
        d=request.POST['pass2']
        if(c != d):
            return HttpResponse("Password does not match...!")
        else:
            data=User.objects.create_user(a,b,c)
            data.save()
            return redirect("/login")
    return render(request, 'register.html') 
   
def login_page(request):
    if request.method == 'POST':
        x=request.POST['name']
        y=request.POST['pass1']

        user=authenticate(request,username=x,password=y)
        if user is not None:
            login(request,user)
            return redirect("/RP")
        else: 
            return HttpResponse("Credentilas Wrong.......!")
    return render(request, 'login.html')    

def logout_page(request):
    logout(request)
    return redirect("/login")