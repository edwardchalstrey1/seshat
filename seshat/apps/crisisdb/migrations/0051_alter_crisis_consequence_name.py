# Generated by Django 4.0.3 on 2023-05-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0050_alter_crisis_consequence_assassination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crisis_consequence',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
