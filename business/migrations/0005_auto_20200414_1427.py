# Generated by Django 3.0.5 on 2020-04-14 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20200413_1934'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TermLoan',
            new_name='BusinessTermLoan',
        ),
    ]
