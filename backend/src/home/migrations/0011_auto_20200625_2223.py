# Generated by Django 3.0.7 on 2020-06-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_patient_occupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='district',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='occupation',
        ),
    ]