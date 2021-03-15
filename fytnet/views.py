from django.shortcuts import render, get_object_or_404
from .models import Fighter


def fighter(request):
    """ A view to return the main fytnet page. """
    fighters = Fighter.objects.all()

    return render(request, "fytnet/fytnet.html", {"fighters": fighters})


def fytnet_profile(request, fighter_id):
    """ A view to show individual fighter profiles """

    fighter = get_object_or_404(Fighter, pk=fighter_id)

    context = {
        "fighter": fighter,
    }

    return render(request, "fytnet/fighter_profile.html", context)
