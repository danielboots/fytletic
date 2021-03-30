from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


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

        messages.success(
            request, "Your message has been submitted, We will get back to you soon"
        )

    return render(request, "contact/contact_new.html")
