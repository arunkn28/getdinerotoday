# Generated by Django 3.0.5 on 2020-04-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0011_revolvingbusinesscreditvendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='revolvingbusinesscreditvendor',
            name='url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startervendorlist',
            name='url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
