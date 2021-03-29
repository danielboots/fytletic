# Generated by Django 3.1.6 on 2021-03-29 15:42

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0018_auto_20210328_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='about',
            field=models.TextField(blank=True, help_text='About the gym.', null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='country',
            field=django_countries.fields.CountryField(blank=True, help_text='What country is this gym located', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='email',
            field=models.CharField(default='gym@fytletic.com', help_text='The Gym email address for enquiries', max_length=50),
        ),
        migrations.AlterField(
            model_name='gym',
            name='facebook',
            field=models.URLField(blank=True, help_text='Link to your Facebook fan or personal page', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='gym_owner',
            field=models.ImageField(blank=True, help_text='Gym owner profile photo', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='gym_owner_name',
            field=models.CharField(blank=True, help_text='Gym owner name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='gym_photo_main',
            field=models.ImageField(blank=True, help_text='Main gym photo displayed as the header to the profile', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='gym_type',
            field=models.ManyToManyField(help_text='What kind of gym is this, what fight discipline does it focus on, or is it a general fitness and wellness center?', to='gym.GymType'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='instagram',
            field=models.URLField(blank=True, help_text='Link to your Instagram', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='is_verified',
            field=models.BooleanField(default=False, help_text='Blue Tick / Not displayed to non admin or form'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='name',
            field=models.CharField(help_text='The Gym Name ie, Golds Gym', max_length=50),
        ),
        migrations.AlterField(
            model_name='gym',
            name='photo_1',
            field=models.ImageField(blank=True, help_text='Images of the gym, interviews or facilities, added to the gallery', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='photo_2',
            field=models.ImageField(blank=True, help_text='Images of the gym, interviews or facilities, added to the gallery', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='photo_3',
            field=models.ImageField(blank=True, help_text='Images of the gym, interviews or facilities, added to the gallery', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='photo_4',
            field=models.ImageField(blank=True, help_text='Images of the gym, interviews or facilities, added to the gallery', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='photo_5',
            field=models.ImageField(blank=True, help_text='Images of the gym, interviews or facilities, added to the gallery', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='photo_6',
            field=models.ImageField(blank=True, help_text='Images of the gym, interviews or facilities, added to the gallery', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='postcode',
            field=models.CharField(blank=True, help_text='Postcode for address', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='street_address1',
            field=models.CharField(blank=True, help_text='Street address, where is this gym located', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='street_address2',
            field=models.CharField(blank=True, help_text='Street address, where is this gym located', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='town_or_city',
            field=models.CharField(blank=True, help_text='The City or Town the gym is located, for example Newcastle Upon Tyne', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='twitter',
            field=models.URLField(blank=True, help_text='Link to your Twitter handle', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='video_1',
            field=models.URLField(blank=True, help_text='Video footage of the gym, interviews or facilities', null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='video_2',
            field=models.URLField(blank=True, help_text='Video footage of the gym, interviews or facilities', null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='video_3',
            field=models.URLField(blank=True, help_text='Video footage of the gym, interviews or facilities', null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='video_4',
            field=models.URLField(blank=True, help_text='Video footage of the gym, interviews or facilities', null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='video_5',
            field=models.URLField(blank=True, help_text='Video footage of the gym, interviews or facilities', null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='web',
            field=models.URLField(blank=True, help_text='Link to your Personal website page', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='whatsapp',
            field=models.CharField(default='5555555555', help_text='The gyms main contact number', max_length=50),
        ),
    ]
