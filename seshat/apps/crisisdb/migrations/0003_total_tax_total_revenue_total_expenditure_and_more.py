# Generated by Django 4.0.3 on 2022-03-07 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_reference_long_name_alter_reference_title'),
        ('crisisdb', '0002_alter_population_total_population'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total_tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Total_tax', max_length=100)),
                ('total_amount_of_taxes_collected', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Total_tax',
                'verbose_name_plural': 'total_taxs',
            },
        ),
        migrations.CreateModel(
            name='Total_revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Total_revenue', max_length=100)),
                ('total_revenue', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Total_revenue',
                'verbose_name_plural': 'total_revenues',
            },
        ),
        migrations.CreateModel(
            name='Total_expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Total_expenditure', max_length=100)),
                ('total_expenditure', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Total_expenditure',
                'verbose_name_plural': 'total_expenditures',
            },
        ),
        migrations.CreateModel(
            name='Total_economic_output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Total_economic_output', max_length=100)),
                ('total_economic_output', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Total_economic_output',
                'verbose_name_plural': 'total_economic_outputs',
            },
        ),
        migrations.CreateModel(
            name='Tariff_and_transit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Tariff_and_transit', max_length=100)),
                ('tariff_and_ransit', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Tariff_and_transit',
                'verbose_name_plural': 'tariff_and_transits',
            },
        ),
        migrations.CreateModel(
            name='Salt_tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Salt_tax', max_length=100)),
                ('salt_tax', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Salt_tax',
                'verbose_name_plural': 'salt_taxs',
            },
        ),
        migrations.CreateModel(
            name='Revenue_real',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Revenue_real', max_length=100)),
                ('revenue_real', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Revenue_real',
                'verbose_name_plural': 'revenue_reals',
            },
        ),
        migrations.CreateModel(
            name='Revenue_official',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Revenue_official', max_length=100)),
                ('revenue_official', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Revenue_official',
                'verbose_name_plural': 'revenue_officials',
            },
        ),
        migrations.CreateModel(
            name='Other_incomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Other_incomes', max_length=100)),
                ('other_incomes', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Other_incomes',
                'verbose_name_plural': 'other_incomess',
            },
        ),
        migrations.CreateModel(
            name='Misc_incomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Misc_incomes', max_length=100)),
                ('misc_incomes', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Misc_incomes',
                'verbose_name_plural': 'misc_incomess',
            },
        ),
        migrations.CreateModel(
            name='Maritime_custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Maritime_custom', max_length=100)),
                ('maritime_custom', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Maritime_custom',
                'verbose_name_plural': 'maritime_customs',
            },
        ),
        migrations.CreateModel(
            name='Lijin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Lijin', max_length=100)),
                ('lijin', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Lijin',
                'verbose_name_plural': 'lijins',
            },
        ),
        migrations.CreateModel(
            name='Land_yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Land_yield', max_length=100)),
                ('land_yield', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Land_yield',
                'verbose_name_plural': 'land_yields',
            },
        ),
        migrations.CreateModel(
            name='Land_taxes_collected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Land_taxes_collected', max_length=100)),
                ('land_taxes_collected', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Land_taxes_collected',
                'verbose_name_plural': 'land_taxes_collecteds',
            },
        ),
        migrations.CreateModel(
            name='Diding_taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Diding_taxes', max_length=100)),
                ('total_revenue', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Diding_taxes',
                'verbose_name_plural': 'diding_taxess',
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Add an Optional description or a personal comment above.', null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Trusted'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Balance', max_length=100)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('citations', models.ManyToManyField(blank=True, help_text='Select one or more references for this fact. Hold CTRL to select multiple.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.polity')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.section')),
                ('subsection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.subsection')),
            ],
            options={
                'verbose_name': 'Balance',
                'verbose_name_plural': 'balances',
            },
        ),
    ]
