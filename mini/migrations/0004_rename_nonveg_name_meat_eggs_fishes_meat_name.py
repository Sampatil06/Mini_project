# Generated by Django 4.2.5 on 2023-10-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0003_milk_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meat_eggs_fishes',
            old_name='nonveg_name',
            new_name='meat_name',
        ),
    ]
