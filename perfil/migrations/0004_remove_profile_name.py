# Generated by Django 3.1 on 2020-10-31 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_profile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
