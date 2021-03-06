# Generated by Django 3.2.8 on 2022-03-30 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rocketTicket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='dependencies',
            field=models.ManyToManyField(blank=True, related_name='_rocketTicket_ticket_dependencies_+', to='rocketTicket.Ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='parentTicket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rocketTicket.ticket'),
        ),
    ]
