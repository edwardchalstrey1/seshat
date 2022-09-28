# Generated by Django 4.0.3 on 2022-09-27 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0015_alter_agricultural_population_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agricultural_population',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='arable_land',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='arable_land_per_farmer',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='crop_failure_event',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='disease_outbreak',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='drought_event',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='external_conflict_side',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='famine_event',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='gdp_per_capita',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='gross_grain_shared_per_agricultural_population',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='internal_conflict',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='locust_event',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='military_expense',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='net_grain_shared_per_agricultural_population',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='silver_inflow',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='silver_stock',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='socioeconomic_turmoil_event',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='surplus',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='total_population',
            unique_together=set(),
        ),
    ]
