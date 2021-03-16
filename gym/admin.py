from django.contrib import admin

from .models import Gym, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Gym)
admin.site.register(Category, CategoryAdmin)
