# Generated by Django 3.0.7 on 2020-07-05 09:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0002_clinicalform_primarydiagnose'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterOfStool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prevalence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='bk',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='calcification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='clinicalform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patientapp.ClinicalForm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='compaction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='decay',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='infiltration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patientapp.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='resorption',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='scarring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='seeding',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='TakingMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromdate', models.DateField(default=datetime.date.today)),
                ('streptomycin', models.BooleanField(default=False)),
                ('rifampicin', models.BooleanField(default=False)),
                ('isoniazid', models.BooleanField(default=False)),
                ('pyrazinamide', models.BooleanField(default=False)),
                ('ethambutol', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuberculosis_tolerance', models.BooleanField(default=False)),
                ('related_disease', models.BooleanField(default=False)),
                ('nausea', models.BooleanField(default=False)),
                ('vomiting', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=False)),
                ('sweating', models.BooleanField(default=False)),
                ('weakness', models.BooleanField(default=False)),
                ('allergodermatosis', models.BooleanField(default=False)),
                ('from_weight_loss', models.FloatField(default=0)),
                ('to_weight_loss', models.FloatField(default=0)),
                ('coproscopy', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Immunogram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd3', models.FloatField(default=0)),
                ('cd4', models.FloatField(default=0)),
                ('cd8', models.FloatField(default=0)),
                ('cd20', models.FloatField(default=0)),
                ('igm', models.FloatField(default=0)),
                ('igg', models.FloatField(default=0)),
                ('iga', models.FloatField(default=0)),
                ('tge', models.FloatField(default=0)),
                ('act', models.FloatField(default=0)),
                ('alt', models.FloatField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diarrhea', models.BooleanField(default=False)),
                ('pyrazinamide', models.BooleanField(default=False)),
                ('ethambutol', models.BooleanField(default=False)),
                ('flatulence', models.BooleanField(default=False)),
                ('stomachache', models.BooleanField(default=False)),
                ('from_stool_frequency', models.IntegerField(default=0)),
                ('to_stool_frequency', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.CharacterOfStool')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='BloodAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('er', models.FloatField(default=0)),
                ('leyk', models.FloatField(default=0)),
                ('hb', models.FloatField(default=0)),
                ('color', models.FloatField(default=0)),
                ('pok', models.FloatField(default=0)),
                ('pya', models.FloatField(default=0)),
                ('sya', models.FloatField(default=0)),
                ('eoz', models.FloatField(default=0)),
                ('lf', models.FloatField(default=0)),
                ('mon', models.FloatField(default=0)),
                ('coe', models.FloatField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='localization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patientapp.Localization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='primarydiagnose',
            name='prevalence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patientapp.Prevalence'),
            preserve_default=False,
        ),
    ]
