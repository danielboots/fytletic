# Generated by Django 3.1.6 on 2021-03-18 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_gym_categorys'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='categorys',
            new_name='categories',
        ),
    ]
