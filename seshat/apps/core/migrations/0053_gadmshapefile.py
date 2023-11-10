# Generated by Django 4.0.3 on 2023-11-10 11:05

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_macrostateshapefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GADMShapefile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('UID', models.BigIntegerField()),
                ('GID_0', models.CharField(max_length=100, null=True)),
                ('NAME_0', models.CharField(max_length=100, null=True)),
                ('VARNAME_0', models.CharField(max_length=100, null=True)),
                ('GID_1', models.CharField(max_length=100, null=True)),
                ('NAME_1', models.CharField(max_length=100, null=True)),
                ('VARNAME_1', models.CharField(max_length=100, null=True)),
                ('NL_NAME_1', models.CharField(max_length=100, null=True)),
                ('ISO_1', models.CharField(max_length=100, null=True)),
                ('HASC_1', models.CharField(max_length=100, null=True)),
                ('CC_1', models.CharField(max_length=100, null=True)),
                ('TYPE_1', models.CharField(max_length=100, null=True)),
                ('ENGTYPE_1', models.CharField(max_length=100, null=True)),
                ('VALIDFR_1', models.CharField(max_length=100, null=True)),
                ('GID_2', models.CharField(max_length=100, null=True)),
                ('NAME_2', models.CharField(max_length=100, null=True)),
                ('VARNAME_2', models.CharField(max_length=100, null=True)),
                ('NL_NAME_2', models.CharField(max_length=100, null=True)),
                ('HASC_2', models.CharField(max_length=100, null=True)),
                ('CC_2', models.CharField(max_length=100, null=True)),
                ('TYPE_2', models.CharField(max_length=100, null=True)),
                ('ENGTYPE_2', models.CharField(max_length=100, null=True)),
                ('VALIDFR_2', models.CharField(max_length=100, null=True)),
                ('GID_3', models.CharField(max_length=100, null=True)),
                ('NAME_3', models.CharField(max_length=100, null=True)),
                ('VARNAME_3', models.CharField(max_length=100, null=True)),
                ('NL_NAME_3', models.CharField(max_length=100, null=True)),
                ('HASC_3', models.CharField(max_length=100, null=True)),
                ('CC_3', models.CharField(max_length=100, null=True)),
                ('TYPE_3', models.CharField(max_length=100, null=True)),
                ('ENGTYPE_3', models.CharField(max_length=100, null=True)),
                ('VALIDFR_3', models.CharField(max_length=100, null=True)),
                ('GID_4', models.CharField(max_length=100, null=True)),
                ('NAME_4', models.CharField(max_length=100, null=True)),
                ('VARNAME_4', models.CharField(max_length=100, null=True)),
                ('CC_4', models.CharField(max_length=100, null=True)),
                ('TYPE_4', models.CharField(max_length=100, null=True)),
                ('ENGTYPE_4', models.CharField(max_length=100, null=True)),
                ('VALIDFR_4', models.CharField(max_length=100, null=True)),
                ('GID_5', models.CharField(max_length=100, null=True)),
                ('NAME_5', models.CharField(max_length=100, null=True)),
                ('CC_5', models.CharField(max_length=100, null=True)),
                ('TYPE_5', models.CharField(max_length=100, null=True)),
                ('ENGTYPE_5', models.CharField(max_length=100, null=True)),
                ('GOVERNEDBY', models.CharField(max_length=100, null=True)),
                ('SOVEREIGN', models.CharField(max_length=100, null=True)),
                ('DISPUTEDBY', models.CharField(max_length=100, null=True)),
                ('REGION', models.CharField(max_length=100, null=True)),
                ('VARREGION', models.CharField(max_length=100, null=True)),
                ('COUNTRY', models.CharField(max_length=100, null=True)),
                ('CONTINENT', models.CharField(max_length=100, null=True)),
                ('SUBCONT', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
