# Generated by Django 3.1.7 on 2021-04-19 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210419_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='openinghours',
            old_name='closingHour',
            new_name='closing_hour',
        ),
        migrations.RenameField(
            model_name='openinghours',
            old_name='openingHour',
            new_name='opening_hour',
        ),
    ]
