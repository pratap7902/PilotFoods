# Generated by Django 3.2.25 on 2024-08-06 10:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pilotapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 10, 47, 0, 235582, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='pilotapp.OrderItem'),
        ),
    ]
