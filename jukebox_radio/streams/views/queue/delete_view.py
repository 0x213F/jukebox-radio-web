import json

from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import F
from django.utils import timezone

from jukebox_radio.core.base_view import BaseView


class QueueDeleteView(BaseView, LoginRequiredMixin):
    def post(self, request, **kwargs):
        """
        When a user "deletes" something from the queue. In this case, what is
        actually happening is queue archival. The queue is deleted in the
        application layer but persists in the database.
        """
        Queue = apps.get_model("streams", "Queue")
        Stream = apps.get_model("streams", "Stream")

        stream = Stream.objects.get(user=request.user)

        queue_uuid = request.POST['queueUuid']
        queue = Queue.objects.get(
            uuid=queue_uuid, stream=stream, user=request.user
        )

        now = timezone.now()
        with transaction.atomic():

            # delete queue
            queue.deleted_at = now
            queue.save()

            # fix offset for up next indexes
            children_queue_count = queue.children.count()
            offset = max(1, children_queue_count)
            relative_up_next = Queue.objects.filter(
                stream=stream, index__gt=queue.index, deleted_at__isnull=True
            )
            relative_up_next.update(index=F('index') - offset)

            # also delete children
            queue.children.all().update(deleted_at=now)

        return self.http_response_200()
