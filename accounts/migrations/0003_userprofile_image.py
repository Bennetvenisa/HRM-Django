# Generated by Django 3.0.8 on 2020-07-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200717_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='noimage.jpg', null=True, upload_to=''),
        ),
    ]
