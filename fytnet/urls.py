from django.urls import path
from . import views

urlpatterns = [
    path("", views.fighter, name="fytnet"),
]
