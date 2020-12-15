from datetime import timedelta

from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.utils import timezone

from jukebox_radio.core.base_view import BaseView


class StreamNextTrackView(BaseView, LoginRequiredMixin):
    def post(self, request, **kwargs):
        """
        When a user wants to play the "up next queue item" right now.
        """
        Track = apps.get_model("music", "Track")
        Collection = apps.get_model("music", "Collection")
        Queue = apps.get_model("streams", "Queue")
        Stream = apps.get_model("streams", "Stream")

        stream = Stream.objects.get(user=request.user)

        try:
            first_queue = Queue.objects.in_stream(stream)[0]
        except IndexError:
            raise ValueError("Queue is empty!")

        playing_at = timezone.now() + timedelta(milliseconds=125)
        with transaction.atomic():

            stream.now_playing = first_queue.track
            stream.played_at = playing_at
            stream.paused_at = None
            stream.save()

            first_queue.played_at = playing_at
            first_queue.is_head = True
            first_queue.save()

            # This condition will only be hit once: when the first queue is
            # created in a stream
            if first_queue.prev_queue_ptr_id:
                first_queue.prev_queue_ptr.is_head = False
                first_queue.prev_queue_ptr.save()

        return self.http_response_200({})
