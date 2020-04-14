# Generated by Django 3.0.5 on 2020-04-14 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20200413_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='lender',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lender',
            name='estimated_amount',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='lender',
            name='terms',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lender',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category'),
        ),
        migrations.AlterField(
            model_name='lender',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='lender',
            name='estimated_term',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lender',
            name='monthly_payment',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='lender',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lender',
            name='payment_terms',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lender',
            name='report_to',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lender',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
