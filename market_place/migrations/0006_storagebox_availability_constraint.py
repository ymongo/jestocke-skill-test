# Generated by Django 4.2.5 on 2023-11-12 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_place', '0005_alter_storagebox_options_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='storagebox',
            constraint=models.CheckConstraint(check=models.Q(('availability_end_date__gt', models.F('availability_start_date'))), name='availability_constraint'),
        ),
    ]