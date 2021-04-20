from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import UserProfile, Leave_allocate
import datetime


# Create your views here.

def register(request):
    
    if request.method=="POST":
        user=request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        designation = request.POST['designation']
        salary= request.POST['salary']
        joining_date= request.POST['joining_date']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exsist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name )
                user.save()
                user_id = User.objects.get(username=user).pk
                user_profile= UserProfile(designation=designation, salary=salary, joining_date= joining_date, user_id=user_id)
                user_profile.save()

                x=datetime.datetime.now()
                n=12-int(x.strftime("%m"))+1
                sl= n*2
                al= n*2
                cl= n*2
                ml= n*3
                pl= n*3
                leave_allo=Leave_allocate(sick_leave=sl, annual_leave=al,casual_leave=cl, maternity_leave=ml, paternity_leave=pl, user_id=user_id)
                leave_allo.save()
                return  redirect('home')           
        else:
            messages.info(request, "Password miss match")
            return redirect('register')
    else:
        return render(request, "registration.html")

def logout(request):
    auth.logout(request)
    return redirect ("login")