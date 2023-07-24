# Generated by Django 4.2.3 on 2023-07-24 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_register_patient_father_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_patient',
            name='Full_Name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
