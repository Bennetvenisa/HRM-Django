from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation= models.CharField(max_length=100)
    salary= models.IntegerField()
    joining_date= models.DateField()
    flag=models.BooleanField(default=False)

class Leave_allocate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sick_leave=models.IntegerField()
    annual_leave=models.IntegerField()
    casual_leave=models.IntegerField()
    maternity_leave=models.IntegerField()
    paternity_leave=models.IntegerField()

 