from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    # Meta Class overwrites Django 'S' to our stated plural metaclass.
    class Meta:
        verbose_name_plural = "Categories"

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
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    # Main
    fighter = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    fight_style = models.CharField(max_length=200, unique=True)
    titles = models.CharField(max_length=200, unique=True)
    bio = models.TextField()
    weight = models.IntegerField(null=True, blank=True)

    # Contact
    email = models.CharField(
        max_length=50, null=False, blank=False, default="DEFAULT VALUE"
    )
    whatsapp = models.CharField(
        max_length=50, null=False, blank=False, default="DEFAULT VALUE"
    )

    # Media
    profile_photo_main = models.ImageField(
        upload_to="media/%Y/%m/%d", null=True, blank=True
    )
    video = models.URLField(null=True, blank=True)
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
