from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "name",
        "phone",
        "message",
        "email",
        "contact_date",
    )

    list_display_links = (
        "user_id",
        "name",
    )

    search_fields = (
        "user_id",
        "name",
    )

    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
