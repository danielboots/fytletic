# Generated by Django 3.1.6 on 2021-02-25 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210225_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
    ]
