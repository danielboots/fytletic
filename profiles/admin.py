from django.contrib import admin

from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "multi_author",
    )


admin.site.register(UserProfile, ProfileAdmin)
