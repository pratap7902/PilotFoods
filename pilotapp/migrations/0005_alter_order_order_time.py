# Generated by Django 3.2.25 on 2024-07-31 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotapp', '0004_alter_order_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 13, 27, 49, 424658)),
        ),
    ]
