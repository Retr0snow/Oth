# Generated by Django 3.1.5 on 2021-01-21 21:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Insert a negative number if you are paying', max_digits=11)),
                ('payee_payer', models.CharField(max_length=50)),
                ('event', models.CharField(choices=[('card', 'Card purchase'), ('save', 'Save'), ('o_transfer_out', 'Own transfer(Send out)'), ('o_transfer_in', 'Own transfer(Send in)'), ('payment', 'Payment transfer'), ('deposit', 'Deposit')], max_length=14)),
                ('message', models.TextField(blank=True, default='This is a default text')),
                ('account_value_before', models.DecimalField(decimal_places=2, default=0, help_text='leave empty, generated automatically', max_digits=11)),
                ('account_value_after', models.DecimalField(decimal_places=2, default=0, help_text='leave empty, generated automatically', max_digits=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_value', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
