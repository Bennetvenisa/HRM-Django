from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from verification.models import Employee_profile



# Create your views here.

def login(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user=auth.authenticate(username=username, password=password)
        
        if user is not None:
                auth.login(request, user)
                return  redirect('home')  
        else:
            messages.info(request, "Invalid Credentials")
            return redirect ("login")

    return render(request, "login.html")

def home(request):
    emp=Employee_profile.objects.all()

    return render(request, "home.html", {'emp':emp})