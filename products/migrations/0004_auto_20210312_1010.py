# Generated by Django 3.1.6 on 2021-03-12 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_memberproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='memberproduct',
            new_name='member',
        ),
    ]