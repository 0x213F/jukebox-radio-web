from datetime import timedelta

from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from jukebox_radio.core.base_view import BaseView
from jukebox_radio.core import time as time_util


class StreamPauseTrackView(BaseView, LoginRequiredMixin):
    def post(self, request, **kwargs):
        """
        When a user pauses a playing stream.
        """
        Track = apps.get_model("music", "Track")
        Collection = apps.get_model("music", "Collection")
        Queue = apps.get_model("streams", "Queue")
        Stream = apps.get_model("streams", "Stream")

        stream = Stream.objects.get(user=request.user)

        if not stream.is_playing:
            raise ValueError("Cannot pause a stream that is not already playing")
        if stream.is_paused:
            raise ValueError("Cannot pause a stream which is already paused")

        pausing_at = time_util.now() + timedelta(milliseconds=100)
        if (stream.started_at - pausing_at) > stream.now_playing_duration:
            raise ValueError(
                "Cannot pause since the track will be over by the time we try to pause"
            )

        stream.paused_at = pausing_at
        stream.save()

        return self.http_response_200(
            {
                "pausedAt": int(stream.paused_at.timestamp()),
            }
        )
