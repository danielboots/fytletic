from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Fighter


def fighter(request):
    """ A view to return the main fytnet page. """
    fighters = Fighter.objects.all()

    # addition of pagination - Followed Traversy media Django dev to deployment.

    paginator = Paginator(fighters, 1)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {"fighters": paged_listings}

    return render(request, "fytnet/fytnet.html", context)


def fytnet_profile(request, fighter_id):
    """ A view to show individual fighter profiles """

    fighter = get_object_or_404(Fighter, pk=fighter_id)

    context = {
        "fighter": fighter,
    }

    return render(request, "fytnet/fighter_profile.html", context)
