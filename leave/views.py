from django.shortcuts import render, redirect
from .forms import leave_apply_form
from django.contrib.auth.models import User
from accounts.models import Leave_allocate
from django.core.mail import send_mail
from django.db import connection

# Create your views here.

def application(request):
    form=leave_apply_form()
    user_id=request.user.id
    allocated= Leave_allocate.objects.get(user_id=user_id)
    cursor=connection.cursor()
    
    if request.method=='POST':
        form= leave_apply_form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user_id= request.user.id

            ####sql codes for checking the leave bank
            if obj.leave_type=='casual_leave':
                if obj.days > allocated.casual_leave:
                    return 

            elif obj.leave=='sick_leave':
                obj.save()
                fromdate_str=str(obj.from_date)
                todate_str=str(obj.to_date)
                send_mail('Application for leave',
                obj.reason + '  from  ' + fromdate_str + '  to  '+ todate_str,
                request.user.email,    #from email
                ['benetvenisa@gmail.com'], #to email
                )
                return redirect ('home')
            else:
                return render(request,"leave_apply.html", {'form': form, 'allocated': allocated})
    else:
        return render(request, "leave_apply.html", {'form': form, 'allocated': allocated})

