# Generated by Django 4.0.3 on 2022-09-19 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_reference_creator_alter_reference_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polity',
            old_name='end',
            new_name='end_year',
        ),
        migrations.RenameField(
            model_name='polity',
            old_name='start',
            new_name='start_year',
        ),
    ]
