# Generated by Django 4.0.3 on 2022-04-02 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rocketTicket', '0005_alter_ticket_children_alter_ticket_dependencies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='longName',
            new_name='longDescription',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='shortName',
            new_name='shortDescription',
        ),
    ]
