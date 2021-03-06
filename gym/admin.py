from django.contrib import admin

from .models import Gym, GymType


class GymTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


admin.site.register(Gym)
admin.site.register(GymType, GymTypeAdmin)
