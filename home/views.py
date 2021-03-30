from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from news.models import Post
from fytnet.models import Fighter
from gym.models import Gym
from contact.models import Contact

# Create your views here.


def index(request):
    """ A view to return the index page. """
    # fix from stackoverflow https://stackoverflow.com/questions/55007405/type-object-book-has-no-attribute-order-by

    posts = Post.objects.order_by("-created_on")[:3]
    fighters = Fighter.objects.order_by("-created_on")[:3]
    gyms = Gym.objects.order_by("-created_on")[:3]

    context = {"posts": posts, "fighters": fighters, "gyms": gyms}

    return render(request, "home/index.html", context)


def about(request):
    """
    A view to return the about page
    """

    return render(request, "home/about.html")


def faq(request):
    """
    A view to return the F.A.Q page
    """

    return render(request, "home/faq.html")


def contact(request):
    """
    A view to return the contact page, using the contact model here !!
    """

    return render(request, "home/contact.html")
