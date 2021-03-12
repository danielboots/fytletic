from django.shortcuts import render
from .models import Fytnet


def fytnet(request):
    """ A view to return the main fytnet page. """
    fytnet = Fytnet.objects.all()

    return render(request, "fytnet/fytnet.html")
