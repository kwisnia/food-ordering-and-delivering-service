# Generated by Django 3.1.7 on 2021-05-28 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210501_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='api.menugroup'),
        ),
        migrations.AlterField(
            model_name='extra',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='api.extragroup'),
        ),
        migrations.AlterField(
            model_name='extragroup',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras_group', to='api.dish'),
        ),
        migrations.AlterField(
            model_name='menugroup',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='api.restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
