from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin

from jukebox_radio.core.base_view import BaseView


class QueueIntervalDeleteView(BaseView, LoginRequiredMixin):
    def post(self, request, **kwargs):
        """
        Delete (archive) a QueueInterval.
        """
        QueueInterval = apps.get_model("streams", "QueueInterval")

        queue_interval_uuid = self.param(request, "queueIntervalUuid")
        queue_interval = QueueInterval.objects.get(uuid=queue_interval_uuid)
        queue_interval.archive()

        # needed for React Redux to update the state on the FE
        queue_uuid = self.param(request, "queueUuid")
        parent_queue_uuid = self.param(request, "parentQueueUuid")

        return self.http_react_response(
            'queueInterval/delete',
            {
                "queueInterval": QueueInterval.objects.serialize(queue_interval),
                "queueUuid": queue_uuid,
                "parentQueueUuid": parent_queue_uuid,
            }
        )