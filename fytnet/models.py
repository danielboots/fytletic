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
        Discipline, null=True, blank=True, on_delete=models.CASCADE
    )

    # Relationship to Weight Class model
    weight_class = models.ForeignKey(
        WeightClass, null=True, blank=True, on_delete=models.CASCADE
    )

    # Relationship to Weight Class model
    trains_at = models.ForeignKey(
        Gym, null=True, blank=True, on_delete=models.CASCADE, related_name="fighters"
    )
    nick_name = models.CharField(
        max_length=50, null=False, blank=False, default="Fytnet PRO Fighter"
    )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    fight_style = models.CharField(max_length=200, unique=False)
    titles = models.CharField(max_length=200, unique=False)
    bio = models.TextField()
    weight = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)

    # Contact
    email = models.CharField(
        max_length=50, null=False, blank=False, default="fighter@fytletic.com"
    )
    whatsapp = models.CharField(
        max_length=50, null=False, blank=False, default="07555555555"
    )

    # Media
    profile_photo_main = models.ImageField(
        upload_to="media/%Y/%m/%d", null=True, blank=True
    )

    video_1 = models.URLField(null=True, blank=True)
    video_2 = models.URLField(null=True, blank=True)
    video_3 = models.URLField(null=True, blank=True)
    video_4 = models.URLField(null=True, blank=True)
    video_5 = models.URLField(null=True, blank=True)

    photo_1 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    photo_2 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    photo_3 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    photo_4 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    photo_5 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    photo_6 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)

    # Social
    facebook = models.URLField(max_length=1024, null=True, blank=True)
    instagram = models.URLField(max_length=1024, null=True, blank=True)
    twitter = models.URLField(max_length=1024, null=True, blank=True)
    web = models.URLField(max_length=1024, null=True, blank=True)

    # Record
    win = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)

    # Misc
    is_verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.first_name


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
