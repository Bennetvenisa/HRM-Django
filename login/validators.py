from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import date


def name_validators(name):
    if not name.isalpha():
        raise ValidationError(_("Invalid name field"))
    else:
        return name

def validate_age(value):
    if int(value) < 18:
        raise ValidationError(_('Invalid Age'))
    else:
        return value

def contact_validate(value):
    if not value.isdigit():
        raise ValidationError(_("Invalid contact no"))
    else:
        return value

def validate_fromdate(date):
    today=date.today()
    if date < today:
        raise ValidationError(_("Enter a valid date"))
    else:
        return date

def validate_days(days):
    if days<=0:
        raise ValidationError(_("Enter a valid date"))
    else:
        return days
