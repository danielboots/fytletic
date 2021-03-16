from django.shortcuts import render, get_object_or_404
from .models import Gym


def gym(request):
    """ A view to return the main fytnet page. """
    gyms = Gym.objects.all()

    return render(request, "gym/gyms.html", {"gyms": gyms})


def gym_profile(request, gym_id):
    """ A view to show individual gyms  """

    gym = get_object_or_404(Gym, pk=gym_id)

    context = {
        "gym": gym,
    }

    return render(
        request,
        "gym/gym_listing.html",
        context,
    )
