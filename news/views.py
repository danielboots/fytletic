from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def news(request):
    """ A view to return the news page. """
    posts = Post.objects.all()

    # addition of pagination - Django dev to deployment.

    paginator = Paginator(posts, 1)
    page = request.GET.get("page")
    paged_posts = paginator.get_page(page)

    context = {"posts": paged_posts}

    return render(request, "news/news.html", context)


@login_required
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
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, "Successfully added comment!")
            return redirect(reverse("news_article", args=[post.slug]))
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


@login_required
def delete_own_comment(request, comment_id, slug):
    """
    Delete own comment / gets comment by post slug and comment id
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, "Comment deleted!")
    return redirect(reverse("news_article", args=[post.slug]))
