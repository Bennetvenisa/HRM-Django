# Generated by Django 3.0.8 on 2020-07-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verify_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('age', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact1', models.CharField(max_length=100)),
                ('contact2', models.CharField(max_length=100)),
            ],
        ),
    ]
