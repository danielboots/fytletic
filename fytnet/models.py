from django.db import models
from django.contrib.auth.models import User


class Fytnet(models.Model):
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
