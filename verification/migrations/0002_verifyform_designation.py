# Generated by Django 3.0.8 on 2020-07-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifyform',
            name='designation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]