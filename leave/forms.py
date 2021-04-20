from django import forms
from .models import Leave_apply


class DateInput(forms.DateInput):
    input_type = 'date'


class leave_apply_form(forms.ModelForm):
    class Meta:
        model=Leave_apply
        exclude=['applied_on', 'user']

        widgets={

            'leave_type':           forms.Select(attrs={'class': 'form-control', 'placeholder': 'Leave_type'}),
            'from_date':            DateInput(attrs={'class': 'form-control'}),
            'to_date':              DateInput(attrs={'class': 'form-control','onchange':"Days()"}),
            'days':                 forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly', 'placeholder':'days'}),
            'reason':               forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'col':5, 'placeholder' : 'reason'}),
            'emergency_contact':    forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'emergency contact no.'}), 
        }
   