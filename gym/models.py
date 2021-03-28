from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class GymType(models.Model):

    # Meta Class overwrites Django 'S' to our stated plural metaclass.
    class Meta:
        verbose_name_plural = "GymTypes"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Gym(models.Model):

    # Main - Used one to one field, one user one Gym profile
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=50, null=False, blank=False)

    # Relationship to Specialises in = aka Gym types
    gym_type = models.ManyToManyField(GymType)

    # Address Fields

    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)

    # Contact
    email = models.CharField(
        max_length=50, null=False, blank=False, default="gym@fytletic.com"
    )
    whatsapp = models.CharField(
        max_length=50, null=False, blank=False, default="5555555555"
    )

    # Owner Details

    gym_owner = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    gym_owner_name = models.CharField(max_length=50, null=True, blank=True)

    # Media
    gym_photo_main = models.ImageField(
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

    # Misc
    about = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
