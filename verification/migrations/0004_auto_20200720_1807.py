# Generated by Django 3.0.8 on 2020-07-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0003_verifyform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifyform',
            name='designation',
            field=models.CharField(max_length=100),
        ),
    ]
