from django.db import models
from django.contrib.auth.models import User


class NewsCategory(models.Model):

    # Meta Class overwrites Django 'S' to our stated plural metaclass.
    class Meta:
        verbose_name_plural = "NewsCategories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):

    # Relationship to Specialises in = aka categories
    categories = models.ManyToManyField(NewsCategory)

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    intro = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Media
    photo_main = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    photo_1 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    photo_2 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


# Comments system


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.user)
