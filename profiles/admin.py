from django.contrib import admin

from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "is_restricted",
    )


admin.site.register(UserProfile, ProfileAdmin)
