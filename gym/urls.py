from django.urls import path
from . import views

urlpatterns = [
    path("", views.gym, name="gym"),
    path("<int:gym_id>/", views.gym_profile, name="gym_profile"),
    path("add/", views.add_gym, name="add_gym"),
    path("edit/<int:fighter_id>/", views.edit_gym, name="edit_gym"),
    path("delete/<int:fighter_id>/", views.delete_gym, name="delete_gym"),
]
