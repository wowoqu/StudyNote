# Generated by Django 2.0.1 on 2018-05-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('f', 'famale'), ('m', 'male')], max_length=1)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('birth', models.DateField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
