# Generated by Django 4.2.2 on 2023-07-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register_Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Middle_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField(default=0)),
                ('Sex', models.CharField(choices=[('Male', 'M'), ('Female', 'F')], default='None', max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=15)),
                ('Emergency_Phone_Number', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Register_Patient',
                'verbose_name_plural': 'Register_Patients',
            },
        ),
    ]
