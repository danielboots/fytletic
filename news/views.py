from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def news(request):
    """ A view to return the news page. """
    posts = Post.objects.all()

    # addition of pagination - Followed Traversy media Django dev to deployment.

    paginator = Paginator(posts, 1)
    page = request.GET.get("page")
    paged_posts = paginator.get_page(page)

    context = {"posts": paged_posts}

    return render(request, "news/news.html", context)


def news_article(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, "news/news_article.html", {"post": post})
