# Generated by Django 3.1 on 2020-08-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='range',
            name='udapte_number',
            field=models.IntegerField(default=1),
        ),
    ]