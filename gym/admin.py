from django.contrib import admin

from .models import Gym, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


admin.site.register(Gym)
admin.site.register(Category, CategoryAdmin)
