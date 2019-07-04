# Generated by Django 2.2 on 2019-06-26 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photos', models.ImageField(upload_to='', verbose_name='photos/%Y/%M/%D')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateField(blank=True, verbose_name=datetime.datetime(2019, 6, 26, 13, 5, 24, 189102))),
            ],
        ),
    ]