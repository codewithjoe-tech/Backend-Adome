# Generated by Django 5.1.6 on 2025-04-27 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_tenantpayments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenantpayments',
            name='bank_account_number',
        ),
        migrations.RemoveField(
            model_name='tenantpayments',
            name='bank_ifsc',
        ),
        migrations.RemoveField(
            model_name='tenantpayments',
            name='email',
        ),
        migrations.RemoveField(
            model_name='tenantpayments',
            name='name',
        ),
    ]
