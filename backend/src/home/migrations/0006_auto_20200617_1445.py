# Generated by Django 3.0.7 on 2020-06-17 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200613_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='height',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='weight',
        ),
    ]
