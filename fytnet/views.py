from django.shortcuts import render
from .models import Fighter


def fighter(request):
    """ A view to return the main fytnet page. """
    fighters = Fighter.objects.all()

    return render(request, "fytnet/fytnet.html")
