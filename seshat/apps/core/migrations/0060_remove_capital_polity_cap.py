# Generated by Django 4.0.3 on 2024-04-04 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_capital_alternative_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capital',
            name='polity_cap',
        ),
    ]
