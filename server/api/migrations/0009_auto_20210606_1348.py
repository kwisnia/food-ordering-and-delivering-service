# Generated by Django 3.1.7 on 2021-06-06 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210528_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Order Placed'), (2, 'Processing'), (3, 'In Delivery'), (4, 'Delivered'), (5, 'Cancelled')], default=1),
        ),
        migrations.AlterField(
            model_name='ordereddish',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='api.order'),
        ),
        migrations.AlterField(
            model_name='orderedextra',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_extras', to='api.ordereddish'),
        ),
    ]
