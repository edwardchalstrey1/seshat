# Generated by Django 4.0.3 on 2023-01-23 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_alter_reference_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citation',
            options={'ordering': ['-created_date']},
        ),
    ]
