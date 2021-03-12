from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    intro = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
