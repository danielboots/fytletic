from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import GymForm
from .models import Gym


def gym(request):
    """ A view to return the main gym page. """
    gyms = Gym.objects.all()
    query = None

    # Search fighter functionality
    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("gym"))

            queries = Q(name__icontains=query) | Q(about__icontains=query)
            gyms = gyms.filter(queries)

    # addition of pagination - Django dev to deployment.

    paginator = Paginator(gyms, 6)
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


@login_required
def add_gym(request):
    """ Add a Gym profile """
    if not request.user.is_authenticated:
        messages.error(request, "Sorry, only logged in members can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = GymForm(request.POST, request.FILES, request.user)
        if form.is_valid():

            gym = form.save(commit=False)
            gym.user = request.user
            gym.save()
            messages.success(request, "Successfully added Gym ")
            return redirect(reverse("gym_profile", args=[gym.id]))
        else:
            messages.error(
                request,
                "Failed to add Gym. Please ensure the form is valid.",
            )
    else:
        form = GymForm()

    template = "gym/add_gym.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


# Edit Gym


@login_required
def edit_gym(request, gym_id):
    """ Edit fight profile """
    if not request.user.is_authenticated:
        messages.error(request, "Sorry, only logged in users can do that.")
        return redirect(reverse("home"))

    gym = get_object_or_404(Gym, pk=gym_id)

    if gym.user != request.user:
        messages.error(request, "Sorry, this isnt your gym!!")
        return redirect(reverse("home"))

    if request.method == "POST" and gym.user == request.user:

        form = GymForm(request.POST, request.FILES, instance=gym)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated Gym")

            return redirect(reverse("gym_profile", args=[gym.id]))
        else:
            messages.error(
                request,
                "Failed to update Your Fight profile. Please ensure the form is valid.",
            )
    else:
        form = GymForm(instance=gym)

        # message
        messages.info(request, f"You are editing {gym.user}")

    template = "gym/edit_gym.html"
    context = {
        "form": form,
        "gym": gym,
    }

    return render(request, template, context)


# Delete Gym


@login_required
def delete_gym(request, gym_id):
    """ Delete a Gym from your profile """
    gym = get_object_or_404(Gym, pk=gym_id)

    if gym.user != request.user:
        messages.error(request, "Sorry, only owners can do that.")
        return redirect(reverse("home"))

    gym.delete()
    messages.success(request, "Gym deleted!")
    return redirect(reverse("profile"))
