from django.shortcuts import render
from django.http import HttpResponse
from news.models import Post

# Create your views here.


def index(request):
    """ A view to return the index page. """
    # fix from stackoverflow https://stackoverflow.com/questions/55007405/type-object-book-has-no-attribute-order-by

    posts = Post.objects.order_by("-created_on")[:3]

    context = {"posts": posts}

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
    A view to return the contact page
    """

    return render(request, "home/contact.html")
