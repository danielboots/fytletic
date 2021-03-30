from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


# Create your views here.


def contact(request):
    """
    A view to return the contact page, using the contact model here !!
    """
    print("test")

    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        contact = Contact(name=name, email=email, phone=phone, message=message)

        contact.save()

        # send email
        send_mail(
            "You have a new message",
            "There has been a message sent from "
            + name
            + ". Login to the admin panel to view.",
            "EMAIL_HOST_USER",
            ["dan@fytletic.com"],
            fail_silently=False,
        )

        messages.success(
            request, "Your message has been submitted, We will get back to you soon"
        )

    return render(request, "contact/contact_new.html")
