# Generated by Django 2.0.1 on 2018-01-26 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_employee_addr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='addr',
        ),
    ]