# Generated by Django 3.0.5 on 2020-04-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0012_auto_20200416_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='nopg',
            name='url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
