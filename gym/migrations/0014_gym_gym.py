# Generated by Django 3.1.6 on 2021-03-27 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0013_auto_20210325_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='gym',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
