# Generated by Django 4.0.3 on 2023-05-24 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_seshat_task_task_url'),
        ('core', '0047_polity_home_nga'),
        ('crisisdb', '0051_alter_crisis_consequence_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crisis_consequence',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Crisis consequence', 'verbose_name_plural': 'Crisis consequences'},
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='assassination',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='capital',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='century_plus',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='civil_war',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='collapse',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='conquest',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='constitution',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='decline',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='depose',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='downward_mobility',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='epidemic',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='extermination',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='fragmentation',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='labor',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='public_goods',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='religion',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='revolution',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='successful_revolution',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='suffrage',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='unfree_labor',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='crisis_consequence',
            name='uprising',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='Power_transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Evidenced'), ('SSP', 'Suspected'), ('IFR', 'Inferred')], default='TRS', max_length=5)),
                ('is_disputed', models.BooleanField(blank=True, default=False, null=True)),
                ('is_uncertain', models.BooleanField(blank=True, default=False, null=True)),
                ('expert_reviewed', models.BooleanField(blank=True, default=True, null=True)),
                ('drb_reviewed', models.BooleanField(blank=True, default=False, null=True)),
                ('predecessor', models.CharField(blank=True, max_length=100, null=True)),
                ('successor', models.CharField(blank=True, max_length=100, null=True)),
                ('reign_number_predecessor', models.IntegerField(blank=True, null=True)),
                ('contested', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('overturn', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('predecessor_assassination', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('intra_elite', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('military_revolt', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('popular_uprising', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('separatist_rebellion', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('external_invasion', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('external_interference', models.CharField(blank=True, choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent'), ('DIS', 'Disputed')], max_length=5, null=True)),
                ('citations', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.seshatcomment')),
                ('curator', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='accounts.seshat_expert')),
                ('polity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.polity')),
            ],
            options={
                'verbose_name': 'Power Transition',
                'verbose_name_plural': 'Power Transitions',
                'ordering': ['year_from', 'year_to'],
            },
        ),
    ]
