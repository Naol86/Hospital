# Generated by Django 4.2.3 on 2023-07-23 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_register_patient_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='register_patient',
            options={'ordering': ['-Created_at']},
        ),
    ]