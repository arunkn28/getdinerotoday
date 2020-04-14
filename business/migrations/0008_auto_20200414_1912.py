# Generated by Django 3.0.5 on 2020-04-14 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_startervendorlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startervendorlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category'),
        ),
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category'),
        ),
    ]
