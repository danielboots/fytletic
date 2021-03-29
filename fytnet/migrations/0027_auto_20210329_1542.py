# Generated by Django 3.1.6 on 2021-03-29 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0019_auto_20210329_1542'),
        ('fytnet', '0026_auto_20210329_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='bio',
            field=models.TextField(help_text='The Fighter Bio, the more indepth the better'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='discipline',
            field=models.ForeignKey(blank=True, help_text='The Fighters main fight discipline', null=True, on_delete=django.db.models.deletion.CASCADE, to='fytnet.discipline'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='draw',
            field=models.IntegerField(default=0, help_text='Fighter Draws'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='email',
            field=models.CharField(blank=True, default='fighter@fytletic.com', help_text='Enter an email address which you dont mind people contacting you at.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='facebook',
            field=models.URLField(blank=True, help_text='Link to your Facebook fan or personal page', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='fight_style',
            field=models.CharField(help_text='Southpaw, orthadox, brawler?', max_length=200),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='first_name',
            field=models.CharField(blank=True, help_text='Enter Fighters real first name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='instagram',
            field=models.URLField(blank=True, help_text='Link to your Instagram', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='is_verified',
            field=models.BooleanField(default=False, help_text='Blue Tick / Not displayed to non admin or form'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='last_name',
            field=models.CharField(blank=True, help_text='Enter Fighters real last name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='location',
            field=models.CharField(blank=True, help_text='Where is this Fighter located', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='loss',
            field=models.IntegerField(default=0, help_text='Fighter Losses'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='nick_name',
            field=models.CharField(blank=True, default='Fytnet PRO Fighter', help_text='The Fighters nick name.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='photo_1',
            field=models.ImageField(blank=True, help_text='Press photos, live action, displayed in Gallery in profile', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='photo_2',
            field=models.ImageField(blank=True, help_text='Press photos, live action, displayed in Gallery in profile', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='photo_3',
            field=models.ImageField(blank=True, help_text='Press photos, live action, displayed in Gallery in profile', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='photo_4',
            field=models.ImageField(blank=True, help_text='Press photos, live action, displayed in Gallery in profile', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='photo_5',
            field=models.ImageField(blank=True, help_text='Press photos, live action, displayed in Gallery in profile', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='photo_6',
            field=models.ImageField(blank=True, help_text='Press photos, live action, displayed in Gallery in profile', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='profile_photo_main',
            field=models.ImageField(blank=True, help_text='The main photo for the Fighter profile header', null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='titles',
            field=models.CharField(help_text='The Main title the Fighter Holds, displayed in head section', max_length=200),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='trains_at',
            field=models.ForeignKey(blank=True, help_text='Where does this Fighter train', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighters', to='gym.gym'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='twitter',
            field=models.URLField(blank=True, help_text='Link to your Twitter Handle', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='video_1',
            field=models.URLField(blank=True, help_text='Video showreel, past fights, interviews, displayed in media section', null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='video_2',
            field=models.URLField(blank=True, help_text='Video showreel, past fights, interviews, displayed in media section', null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='video_3',
            field=models.URLField(blank=True, help_text='Video showreel, past fights, interviews, displayed in media section', null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='video_4',
            field=models.URLField(blank=True, help_text='Video showreel, past fights, interviews, displayed in media section', null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='video_5',
            field=models.URLField(blank=True, help_text='Video showreel, past fights, interviews, displayed in media section', null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='web',
            field=models.URLField(blank=True, help_text='Link to your Personal Website', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='weight',
            field=models.IntegerField(blank=True, help_text='This is the weight of the fighter please use lbs', null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='weight_class',
            field=models.ForeignKey(blank=True, help_text='What is the Fighters main weight class.', null=True, on_delete=django.db.models.deletion.CASCADE, to='fytnet.weightclass'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='whatsapp',
            field=models.CharField(blank=True, default='07555555555', help_text='Your contact phone number', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='win',
            field=models.IntegerField(default=0, help_text='Fighter Wins'),
        ),
    ]
