from django.db import models
from django.contrib.auth.models import User
from login.validators import validate_fromdate, validate_days

# Create your models here.

class Leave_apply(models.Model):
    leave_types=[
        ('sick_leave', 'Sick Leave'),
        ('annual_leave', 'Annual Leave'),
        ('casual_leave', 'Casual Leave'),
        ('maternity_leave', 'Maternity Leave'),
        ('paternity_leave', 'paternity Leave')
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type= models.CharField(max_length=100, choices=leave_types)
    applied_on= models.DateField(auto_now=True)
    from_date=  models.DateField(validators=[validate_fromdate])
    to_date=    models.DateField()
    days=       models.IntegerField(validators=[validate_days])
    reason=     models.TextField()
    emergency_contact= models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Leave_apply, self).save(*args, **kwargs)

