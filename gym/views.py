from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gym


def gym(request):
    """ A view to return the main fytnet page. """
    gyms = Gym.objects.all()

    # addition of pagination - Followed Traversy media Django dev to deployment.

    paginator = Paginator(gyms, 1)
    page = request.GET.get("page")
    paged_gyms = paginator.get_page(page)

    context = {"gyms": paged_gyms}

    return render(request, "gym/gyms.html", context)


def gym_profile(request, gym_id):
    """ A view to show individual gyms  """

    gym = get_object_or_404(Gym, pk=gym_id)

    context = {
        "gym": gym,
        "fighters": gym.fighters.all(),  # Fighter.objects.filter(trains_at=gym).all()
    }

    # get_absolute_url to get the url for the fighter or gym

    return render(
        request,
        "gym/gym_listing.html",
        context,
    )
