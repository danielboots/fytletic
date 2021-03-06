from django.contrib import admin

from .models import Post, NewsCategory, Comment


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post)

admin.site.register(NewsCategory, NewsCategoryAdmin)
