from django.contrib import admin

from .models import Fighter, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Fighter)
admin.site.register(Category, CategoryAdmin)
