# Generated by Django 3.2.8 on 2021-10-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic/DoctorProfilePic/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic/PatientProfilePic/'),
        ),
    ]
