from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

from fytnet.models import Fighter
from gym.models import Gym

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    multi_author = profile.multi_author

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:

        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    # importing fighters and gym to profile view - and context

    fighters = Fighter.objects.filter(user=request.user).order_by("-created_on")[:10]
    gyms = Gym.objects.filter(user=request.user).order_by("-created_on")[:10]

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "fighters": fighters,
        "gyms": gyms,
        "on_profile_page": True,
        "multi_author": multi_author,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
