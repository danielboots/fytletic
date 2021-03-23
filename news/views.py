from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


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

    template_name = "news/news_article.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
