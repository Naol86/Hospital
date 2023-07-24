# Generated by Django 4.2.3 on 2023-07-24 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_register_patient_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_patient',
            name='Father_Name',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register_patient',
            name='Mother_Name',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]