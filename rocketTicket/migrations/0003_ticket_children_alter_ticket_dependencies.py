# Generated by Django 4.0.3 on 2022-04-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocketTicket', '0002_auto_20220330_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='children',
            field=models.ManyToManyField(blank=True, to='rocketTicket.ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dependencies',
            field=models.ManyToManyField(blank=True, to='rocketTicket.ticket'),
        ),
    ]
