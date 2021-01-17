import uuid

from django.db import models

import pgtrigger

from jukebox_radio.core import time as time_util


class MarkerManager(models.Manager):
    def serialize(self, marker):
        if not marker:
            return None

        return {
            "uuid": marker.uuid,
            "trackUuid": marker.track_id,
            "timestampMilliseconds": marker.timestamp_ms,
        }


@pgtrigger.register(
    pgtrigger.Protect(
        name="append_only",
        operation=(pgtrigger.Update | pgtrigger.Delete),
    )
)
class Marker(models.Model):
    """
    A bookmark to a book is like a marker to a track. A user may set markers on
    a track to indicate points of interest. For example, you might want to set
    a marker at the beginning of a solo.
    """
    objects = MarkerManager()

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    track = models.ForeignKey(
        "music.Track",
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
    )

    timestamp_ms = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.deleted_at = time_util.now()
        self.save()
