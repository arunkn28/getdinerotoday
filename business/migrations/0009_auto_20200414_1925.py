# Generated by Django 3.0.5 on 2020-04-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_auto_20200414_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenuelending',
            old_name='registerd_at',
            new_name='registered_at',
        ),
    ]
