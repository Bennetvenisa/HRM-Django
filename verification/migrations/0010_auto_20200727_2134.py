# Generated by Django 3.0.8 on 2020-07-27 16:04

from django.db import migrations, models
import login.validators


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0009_auto_20200727_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_profile',
            name='middle_name',
            field=models.CharField(max_length=100, null=True, validators=[login.validators.name_validators]),
        ),
    ]