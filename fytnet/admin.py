from django.contrib import admin

from .models import Fighter, Discipline, WeightClass


class DisciplineAdmin(admin.ModelAdmin):
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
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(WeightClass, WeightClassAdmin)
