# Generated by Django 4.2.3 on 2023-07-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_register_patient_is_active_for_nurse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_patient',
            name='is_Active_For_Nurse',
        ),
        migrations.AddField(
            model_name='register_patient',
            name='Nurse_Checked',
            field=models.BooleanField(default=False),
        ),
    ]
