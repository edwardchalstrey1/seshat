# Generated by Django 4.0.3 on 2022-11-28 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_capital_options_alter_capital_latitude_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seshatcommentpart',
            options={'ordering': ['comment_order']},
        ),
    ]
