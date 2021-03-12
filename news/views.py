from django.shortcuts import render
from .models import Post


def news(request):
    """ A view to return the news page. """
    posts = Post.objects.all()

    return render(request, "news/news.html", {"posts": posts})


def news_article(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, "news/news_article.html", {"post": post})
