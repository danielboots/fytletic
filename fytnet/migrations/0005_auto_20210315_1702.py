# Generated by Django 3.1.6 on 2021-03-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fytnet', '0004_auto_20210315_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='draw',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fighter',
            name='email',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='fighter',
            name='facebook',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fighter',
            name='instagram',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fighter',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fighter',
            name='loss',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fighter',
            name='twitter',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fighter',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fighter',
            name='web',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fighter',
            name='whatsapp',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='fighter',
            name='win',
            field=models.IntegerField(default=0),
        ),
    ]
