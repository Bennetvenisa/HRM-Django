from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import Employee_profile, Employee_edu


# Create your views here.
def verification(request):
    user=request.user
    user_id=User.objects.get(username=user).pk

    if request.method=='POST':
        salutation=request.POST['salutation']
        first_name=user.first_name
        middle_name= request.POST['middle_name']
        last_name=user.last_name
        designation=user.userprofile.designation
        birth_date=request.POST['birth_date']
        email=user.email
        salary=user.userprofile.salary
        age=request.POST['age']
        gender= request.POST['gender']
        address=request.POST['address']
        state= request.POST['state']
        city= request.POST['city']
        pincode= request.POST['pincode']
        contact1= request.POST['contact1']
        contact2= request.POST['contact2']
        image= request.FILES['document']
        fs=FileSystemStorage()
        fs.save(image.name, image)


        user=Employee_profile(salutation=salutation, first_name=first_name, middle_name=middle_name, last_name=last_name, birth_date=birth_date, user_id=user_id, email=email,
        designation=designation, salary=salary, age=age, gender=gender, address=address, state=state, city=city, pincode=pincode, contact1=contact1, contact2=contact2, image=image.name)
        user.save()
        ## automatic leaves allocation##
        ##join_d=user.userprofile.joining_date


         

        return  redirect('verify_form2')

    else:
        if Employee_profile.objects.filter(user_id=user_id).exists():
            return redirect('profile')
        else:
            return render(request, "verify.html")


def profile(request):
    user_id=request.user.id
    employee= Employee_profile.objects.get(user_id=user_id)
    return render (request, "profile.html", {'employee': employee})

def verify_form2(request):
    user=request.user
    user_id=User.objects.get(username=user).pk

    if request.method=='POST':
        highest_degree= request.POST['highest_degree']
        degree_type= request.POST['degree_type']
        specialization= request.POST['specialization']
        college= request.POST['college']
        university= request.POST['university']
        program_type= request.POST['program_type']
        graduated= request.POST['graduated']
        graduated_on= request.POST['graduated_on']


        user=Employee_edu(highest_degree= highest_degree, degree_type= degree_type, specialization= specialization, 
        college= college, university= university, program_type= program_type, graduated= graduated, graduated_on= graduated_on, user_id=user_id)
        user.save()
        return  redirect('home')

    else:
        if Employee_edu.objects.filter(user_id=user_id).exists():
            return redirect('profile')
        else:
            return render(request, "verify_form2.html")