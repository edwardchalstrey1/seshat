# Generated by Django 4.0.3 on 2023-02-06 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_citation_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='polity',
            options={'ordering': ['long_name']},
        ),
    ]
