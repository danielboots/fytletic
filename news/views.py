from django.shortcuts import render
from django.urls import path


def news(request):
    """ A view to return the news page. """

    return render(request, "news/news.html")
