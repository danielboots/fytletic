# Generated by Django 3.1.6 on 2021-03-25 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fytnet', '0011_auto_20210325_0848'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Discipline',
        ),
        migrations.AlterModelOptions(
            name='discipline',
            options={'verbose_name_plural': 'Disciplines'},
        ),
    ]