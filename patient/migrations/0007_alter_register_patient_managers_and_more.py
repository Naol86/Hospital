# Generated by Django 4.2.3 on 2023-07-24 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_register_patient_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='register_patient',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='register_patient',
            name='Birth_Day',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
