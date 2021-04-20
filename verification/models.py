from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, validate_email
from django.utils.translation import gettext_lazy as _
from login.validators import name_validators, validate_age, contact_validate

# Create your model

class Employee_profile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default= "noimage.jpg", null=True)
    salutation=models.CharField(max_length=10, null=True)
    first_name= models.CharField(max_length=100, null=True)
    middle_name= models.CharField(max_length=100, null=True, validators=[name_validators])
    last_name=models.CharField(max_length=100, null=True)
    designation= models.CharField(max_length=100, null=True)
    email=models.EmailField(null=True)
    birth_date=models.DateField()
    age=models.CharField(max_length=20, null=True, validators=[validate_age])
    gender= models.CharField(max_length=20, null=True )
    address=models.TextField(null=True)
    state= models.CharField(max_length=100, null=True,)
    city= models.CharField(max_length=100, null=True,)  
    salary=models.IntegerField()
    pincode= models.CharField(max_length=100, null=True)
    contact1= models.CharField(max_length=12, null=True)
    contact2= models.CharField(max_length=12, null=True)
    verified_on=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Employee_profile, self).save(*args, **kwargs)



class Employee_edu(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    highest_degree= models.CharField(max_length=100, null=True)
    degree_type= models.CharField(max_length=100, null=True)
    specialization=models.CharField(max_length=100, null=True, validators=[name_validators])
    college= models.CharField(max_length=100, null=True, validators=[name_validators])
    university= models.CharField(max_length=100, null=True, validators=[name_validators])
    program_type= models.CharField(max_length=20, null=True)
    graduated= models.CharField(max_length=20, null=True)
    graduated_on= models.DateField()




    



