# Generated by Django 4.1.3 on 2022-11-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_patient_patientusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(default='nope@nope.nope', max_length=120),
        ),
    ]
