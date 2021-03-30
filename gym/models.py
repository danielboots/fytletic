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

    name = models.CharField(
        max_length=50, null=False, blank=False, help_text="The Gym Name ie, Golds Gym"
    )

    # Relationship to Specialises in = aka Gym types
    gym_type = models.ManyToManyField(
        GymType,
        help_text="What kind of gym is this, what fight discipline does it focus on, or is it a general fitness and wellness center?",
    )

    # Address Fields

    street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="Street address, where is this gym located",
    )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="Street address, where is this gym located",
    )
    country = CountryField(
        blank_label="Country *",
        null=True,
        blank=True,
        help_text="What country is this gym located",
    )
    postcode = models.CharField(
        max_length=20, null=True, blank=True, help_text="Postcode for address"
    )
    town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        help_text="The City or Town the gym is located, for example Newcastle Upon Tyne",
    )

    # Contact
    email = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default="gym@fytletic.com",
        help_text="The Gym email address for enquiries",
    )
    whatsapp = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default="5555555555",
        help_text="The gyms main contact number",
    )

    # Owner Details

    gym_owner = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Gym owner profile photo",
    )
    gym_owner_name = models.CharField(
        max_length=50, null=True, blank=True, help_text="Gym owner name"
    )

    # Media
    gym_photo_main = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Main gym photo displayed as the header to the profile",
    )
    video_1 = models.URLField(
        null=True,
        blank=True,
        help_text="Video footage of the gym, interviews or facilities",
    )
    video_2 = models.URLField(
        null=True,
        blank=True,
        help_text="Video footage of the gym, interviews or facilities",
    )
    video_3 = models.URLField(
        null=True,
        blank=True,
        help_text="Video footage of the gym, interviews or facilities",
    )
    video_4 = models.URLField(
        null=True,
        blank=True,
        help_text="Video footage of the gym, interviews or facilities",
    )
    video_5 = models.URLField(
        null=True,
        blank=True,
        help_text="Video footage of the gym, interviews or facilities",
    )

    photo_1 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Images of the gym, interviews or facilities, added to the gallery",
    )
    photo_2 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Images of the gym, interviews or facilities, added to the gallery",
    )
    photo_3 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Images of the gym, interviews or facilities, added to the gallery",
    )
    photo_4 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Images of the gym, interviews or facilities, added to the gallery",
    )
    photo_5 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Images of the gym, interviews or facilities, added to the gallery",
    )
    photo_6 = models.ImageField(
        upload_to="media/%Y/%m/%d",
        null=True,
        blank=True,
        help_text="Images of the gym, interviews or facilities, added to the gallery",
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
        max_length=1024, null=True, blank=True, help_text="Link to your Twitter handle"
    )
    web = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        help_text="Link to your Personal website page",
    )

    # Misc
    about = models.TextField(null=True, blank=True, help_text="About the gym.")
    is_verified = models.BooleanField(
        default=False, help_text="Blue Tick / Not displayed to non admin or form"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
