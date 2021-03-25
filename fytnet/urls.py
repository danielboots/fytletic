from django.urls import path
from . import views

urlpatterns = [
    path("", views.fighter, name="fytnet"),
    path("<int:fighter_id>/", views.fytnet_profile, name="fytnet_profile"),
    path("add/", views.add_fighter, name="add_fighter"),
    path("edit/<int:fighter_id>/", views.edit_fighter, name="edit_fighter"),
    path("delete/<int:fighter_id>/", views.delete_fighter, name="delete_fighter"),
]
