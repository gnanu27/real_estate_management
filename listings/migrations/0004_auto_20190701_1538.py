# Generated by Django 2.2 on 2019-07-01 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20190626_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 15, 38, 17, 624336)),
        ),
    ]