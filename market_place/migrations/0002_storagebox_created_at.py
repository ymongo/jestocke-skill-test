# Generated by Django 4.2.5 on 2023-11-10 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market_place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagebox',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
