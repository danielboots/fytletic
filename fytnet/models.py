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


class Fighter(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    fighter = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    fight_style = models.CharField(max_length=200, unique=True)
    titles = models.CharField(max_length=200, unique=True)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.fighter
