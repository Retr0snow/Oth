# Generated by Django 3.1.5 on 2021-02-23 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210212_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_value',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2021, 2, 23), null=True),
        ),
        migrations.AlterField(
            model_name='movements',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2021, 2, 23), null=True),
        ),
    ]
