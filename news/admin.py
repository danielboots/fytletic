from django.contrib import admin

from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
