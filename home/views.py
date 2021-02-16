from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page. """

    return render(request, "home/index.html")


def about(request):
    """
    A view to return the about page
    """

    return render(request, "home/about.html")


def contact(request):
    """
    A view to return the contact page
    """

    return render(request, "home/contact.html")


def dan(request):
    """
    A view to return the Dan page
    """

    return render(request, "home/dan.html")
