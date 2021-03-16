from django.urls import path
from . import views

urlpatterns = [
    path("", views.gym, name="gym"),
    path("<int:gym_id>/", views.gym_profile, name="gym_profile"),
]
