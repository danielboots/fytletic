# Generated by Django 3.1.6 on 2021-03-16 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='first_name',
            new_name='name',
        ),
    ]