# Generated by Django 3.1.5 on 2021-02-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_movements_move_to_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='movements',
            name='move_to_account',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
