from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import FighterForm
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


# Edit Fight Profile


@login_required
def add_fighter(request):
    """ Add a Fighter to your profile """
    if not request.user.is_authenticated:
        messages.error(request, "Sorry, only logged in members can do that.")
        return redirect(reverse("home"))

    # requesting the logged in user

    if request.method == "POST" and request.user.is_authenticated:
        form = FighterForm(request.POST, request.FILES, request.user)

        if form.is_valid():

            fighter = form.save()
            messages.success(request, "Successfully added Fighter Profile!")
            return redirect(reverse("fytnet_profile", args=[fighter.id]))
        else:
            messages.error(
                request,
                "Failed to add Fighter profile. Please ensure the form is valid.",
            )
    else:
        form = FighterForm()

    template = "fytnet/add_fighter.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


# Edit Fighter Profile


@login_required
def edit_fighter(request, fighter_id):
    """ Edit fight profile """
    if not request.user.is_authenticated:
        messages.error(request, "Sorry, only logged in users can do that.")
        return redirect(reverse("home"))

    fighter = get_object_or_404(Fighter, pk=fighter_id)
    if request.method == "POST" and request.user.is_authenticated:
        form = FighterForm(request.POST, request.FILES, instance=fighter)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated Fight Profile!")

            return redirect(reverse("fytnet_profile", args=[fighter.id]))
        else:
            messages.error(
                request,
                "Failed to update Your Fight profile. Please ensure the form is valid.",
            )
    else:
        form = FighterForm(instance=fighter)

        # This line doesnt work.
        messages.info(request, f"You are editing {fighter.user}")

    template = "fytnet/edit_fighter.html"
    context = {
        "form": form,
        "fighter": fighter,
    }

    return render(request, template, context)


# Delete Fighter Profile


@login_required
def delete_fighter(request, fighter_id):
    """ Delete a Fighter from your profile """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only owners can do that.")
        return redirect(reverse("home"))

    fighter = get_object_or_404(Fighter, pk=fighter_id)
    fighter.delete()
    messages.success(request, "Fighter deleted!")
    return redirect(reverse("profile"))
