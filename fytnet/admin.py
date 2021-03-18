from django.contrib import admin

from .models import Fighter, Category, WeightClass


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


class WeightClassAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


admin.site.register(Fighter)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WeightClass, WeightClassAdmin)
