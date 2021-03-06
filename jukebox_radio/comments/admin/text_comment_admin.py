import pghistory
from django.apps import apps
from django.contrib import admin


@admin.register(apps.get_model("comments.TextComment"))
class TextCommentAdmin(admin.ModelAdmin):

    order_by = ("created_at",)

    list_display = (
        "uuid",
        "text",
        "created_at",
        "user",
    )

    def get_queryset(self, request):
        ABCNotation = apps.get_model("comments", "ABCNotation")
        qs = super().get_queryset(request)
        qs = qs.filter(format=ABCNotation.FORMAT_TEXT)
        qs = qs.order_by("created_at")
        return qs

    def has_add_permission(self, request, obj=None):
        return False

    # NOTE: https://github.com/jyveapp/django-pghistory
    object_history_template = "admin/pghistory_template.html"

    def history_view(self, request, object_id, extra_context=None):
        """
        Adds additional context for the custom history template.
        """
        extra_context = extra_context or {}
        extra_context["object_history"] = (
            pghistory.models.AggregateEvent.objects.target(self.model(pk=object_id))
            .order_by("pgh_created_at")
            .select_related("pgh_context")
        )
        return super().history_view(request, object_id, extra_context=extra_context)
