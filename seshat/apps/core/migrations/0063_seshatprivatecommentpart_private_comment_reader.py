# Generated by Django 4.0.3 on 2024-04-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_seshat_task_task_url'),
        ('core', '0062_polity_private_comment_n'),
    ]

    operations = [
        migrations.AddField(
            model_name='seshatprivatecommentpart',
            name='private_comment_reader',
            field=models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_readers_related', related_query_name='%(app_label)s_%(class)ss_readers', to='accounts.seshat_expert'),
        ),
    ]
