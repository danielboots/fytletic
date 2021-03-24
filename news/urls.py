from django.urls import path
from . import views

urlpatterns = [
    path("", views.news, name="news"),
    path("<slug:slug>/", views.news_article, name="news_article"),
    path(
        "delete/<slug:slug>/<int:comment_id>",
        views.delete_own_comment,
        name="delete_own_comment",
    ),
]
