# Generated by Django 3.0.7 on 2020-07-17 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0012_remove_initialquestion_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='initialquestion',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='initialquestion',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='initialquestion',
            name='questions',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
