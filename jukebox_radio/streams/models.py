import pgtrigger
import uuid

from django.db import models

import pghistory
import pgtrigger
from unique_upload import unique_upload


@pgtrigger.register(
    pgtrigger.Protect(
        name='protect_deletes',
        operation=pgtrigger.Delete
    )
)
@pghistory.track(pghistory.Snapshot('stream.snapshot'))
class Stream(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    now_playing = models.ForeignKey('music.Track', on_delete=models.CASCADE)
    played_at = models.DateTimeField()
    is_playing = models.BooleanField()

    recording_started_at = models.DateTimeField()
    recording_ended_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@pgtrigger.register(
    pgtrigger.Protect(
        name='protect_deletes',
        operation=pgtrigger.Delete
    )
)
class Queue(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    track = models.ForeignKey(
        'music.Track',
        related_name='+',
        on_delete=models.CASCADE,
    )
    collection = models.ForeignKey(
        'music.Collection',
        related_name='+',
        on_delete=models.CASCADE,
    )

    stream = models.ForeignKey(
        'streams.Stream',
        related_name='+',
        on_delete=models.CASCADE,
    )
    prev_queue_ptr = models.ForeignKey(
        'streams.Queue',
        related_name='+',
        on_delete=models.CASCADE,
    )
    next_queue_ptr = models.ForeignKey(
        'streams.Queue',
        related_name='+',
        on_delete=models.CASCADE,
    )

    is_abstract = models.BooleanField()
    parent_queue_ptr = models.ForeignKey(
        'streams.Queue',
        related_name='+',
        on_delete=models.CASCADE,
    )

    played_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
