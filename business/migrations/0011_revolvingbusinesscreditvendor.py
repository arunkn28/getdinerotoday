# Generated by Django 3.0.5 on 2020-04-16 13:47

import business.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_businesscreditcard_personalcreditcard_personalloan'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevolvingBusinessCreditVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('terms', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category')),
            ],
            options={
                'db_table': 'revolving_business_credit',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
    ]
