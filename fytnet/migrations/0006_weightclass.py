# Generated by Django 3.1.6 on 2021-03-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fytnet', '0005_auto_20210315_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'WeightClasses',
            },
        ),
    ]