# Generated by Django 4.0.4 on 2022-05-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poonam', '0002_booking_expected_checkout_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='floor_name',
            field=models.IntegerField(unique=True),
        ),
    ]
