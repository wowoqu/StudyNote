# Generated by Django 2.0.1 on 2018-01-26 09:37

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
                ('addr', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]