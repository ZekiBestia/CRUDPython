# Generated by Django 3.2.8 on 2023-11-19 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Panaderia', '0002_panes_stock'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Panes',
            new_name='Pan',
        ),
    ]
