from django.urls import path
from . import views

urlpatterns = [
    path("", views.fighter, name="fytnet"),
    path("<int:fighter_id>/", views.fytnet_profile, name="fytnet_profile"),
]
