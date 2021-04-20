# Generated by Django 3.0.8 on 2020-07-28 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('verification', '0010_auto_20200727_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_edu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_degree', models.CharField(max_length=100, null=True)),
                ('degree_type', models.CharField(max_length=100, null=True)),
                ('specialization', models.CharField(max_length=100, null=True)),
                ('college', models.CharField(max_length=100, null=True)),
                ('university', models.CharField(max_length=100, null=True)),
                ('program_type', models.CharField(max_length=20, null=True)),
                ('graduated', models.CharField(max_length=20, null=True)),
                ('graduated_on', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
