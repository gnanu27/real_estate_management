# Generated by Django 2.2 on 2019-07-01 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20190626_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 7, 1, 15, 38, 17, 624336)),
        ),
    ]
