from django.db import models
from django.contrib.auth.models import User
from gym.models import Gym

# fight profile update and save

from django.db.models.signals import post_save
from django.dispatch import receiver


class Discipline(models.Model):

    # Meta Class overwrites Django 'S' to our stated plural metaclass.
    class Meta:
        verbose_name_plural = "Disciplines"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WeightClass(models.Model):

    # Meta Class overwrites Django 'S' to our stated plural metaclass.
    class Meta:
        verbose_name_plural = "WeightClasses"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Fighter(models.Model):

    # Main - Used one to one field, one user one fighter profile.

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Relationship to Fighter discipline in = aka categories

    discipline = models.ForeignKey(
        Discipline,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="The Fighters main fight discipline",
    )

    # Relationship to Weight Class model
    weight_class = models.ForeignKey(
        WeightClass,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="What is the Fighters main weight class.",
    )

    # Relationship to Weight Class model
    trains_at = models.ForeignKey(
        Gym,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="fighters",
        help_text="Where does this Fighter train",
    )
    nick_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Fytnet PRO Fighter",
        help_text="The Fighters nick name.",
    )

    first_name = models.CharField(
        max_length=50, null=True, blank=True, help_text="Enter Fighters real first name"
    )
    last_name = models.CharField(
        max_length=50, null=True, blank=True, help_text="Enter Fighters real last name"
    )
    fight_style = models.CharField(
        max_length=200, unique=False, help_text="Southpaw, orthadox, brawler?"
    )
    titles = models.CharField(
        max_length=200,
        unique=False,
        help_text="The Main title the Fighter Holds, displayed in head section",
    )
    bio = models.TextField(help_text="The Fighter Bio, the more indepth the better")
    weight = models.IntegerField(
        null=True,
        blank=True,
        help_text="This is the weight of the fighter please use lbs",
    )
    location = models.CharField(
        max_length=50, null=True, blank=True, help_text="Where is this Fighter located"
    )

    # Contact
    email = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="fighter@fytletic.com",
        help_text="Enter an email address which you dont mind people contacting you at.",
    )
    whatsapp = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="07555555555",
        help_text="Your contact phone number",
    )

    # Media
    profile_photo_main = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=False,
        blank=False,
        help_text="The main photo for the Fighter profile header",
    )

    video_1 = models.URLField(
        null=True,
        blank=True,
        help_text="Video showreel, past fights, interviews, displayed in media section",
    )
    video_2 = models.URLField(
        null=True,
        blank=True,
        help_text="Video showreel, past fights, interviews, displayed in media section",
    )
    video_3 = models.URLField(
        null=True,
        blank=True,
        help_text="Video showreel, past fights, interviews, displayed in media section",
    )
    video_4 = models.URLField(
        null=True,
        blank=True,
        help_text="Video showreel, past fights, interviews, displayed in media section",
    )
    video_5 = models.URLField(
        null=True,
        blank=True,
        help_text="Video showreel, past fights, interviews, displayed in media section",
    )

    photo_1 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Press photos, live action, displayed in Gallery in profile",
    )
    photo_2 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Press photos, live action, displayed in Gallery in profile",
    )
    photo_3 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Press photos, live action, displayed in Gallery in profile",
    )
    photo_4 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Press photos, live action, displayed in Gallery in profile",
    )
    photo_5 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Press photos, live action, displayed in Gallery in profile",
    )
    photo_6 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Press photos, live action, displayed in Gallery in profile",
    )

    # Social
    facebook = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        help_text="Link to your Facebook fan or personal page",
    )
    instagram = models.URLField(
        max_length=1024, null=True, blank=True, help_text="Link to your Instagram"
    )
    twitter = models.URLField(
        max_length=1024, null=True, blank=True, help_text="Link to your Twitter Handle"
    )
    web = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        help_text="Link to your Personal Website",
    )

    # Record
    win = models.IntegerField(default=0, help_text="Fighter Wins")
    draw = models.IntegerField(default=0, help_text="Fighter Draws")
    loss = models.IntegerField(default=0, help_text="Fighter Losses")

    # Misc
    is_verified = models.BooleanField(
        default=False, help_text="Blue Tick / Not displayed to non admin or form"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# If created or update for users profile only


@receiver(post_save, sender=User)
def create_or_update_user_fighter(sender, instance, created, **kwargs):
    """
    Create or update the users Fighter profile
    """
    if created:
        Fighter.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
