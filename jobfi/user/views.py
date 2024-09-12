from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . forms import CustomRegistration

def userlogin(request):
    user = None
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.object.create(username=username,password=password)
        except Exception as e:
            error_message = str(e)
            # return redirect('home')
    return render (request,'applicants/login.html',{'user':user,'error_message':error_message})

def userregistration(request):
    form_registration = CustomRegistration
    if request.method == 'POST':
        form_registration = CustomRegistration(request.POST,request.FILES)
        if form_registration.is_valid():
            form_registration.save()
            return redirect('login')
    return render(request,'applicants/signup.html',{'form_registration':form_registration})

def home(request):
    return render(request,'applicants/home.html')