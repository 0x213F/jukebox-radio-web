from django.core.serializers import serialize
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseRedirect,
    JsonResponse,
)
from django.template.response import TemplateResponse

import contextlib
from django_pglocks import advisory_lock
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class BaseView(APIView):
    """
    Inherits from Django View.
    """

    permission_classes = (IsAuthenticated,)

    def param(self, request, key):
        if request.method == 'GET':
            obj = request.GET
        elif request.method == 'POST':
            obj = request.POST
        else:
            raise ValueError('Unsupported request method')

        val = obj[key]
        if val == 'null':
            return None
        if val == 'undefined':
            return None
        if val == 'true':
            return True
        if val == 'false':
            return False
        return val

    @contextlib.contextmanager
    def acquire_playback_control_lock(self, stream):
        lock_id = f'stream-{stream.uuid}'
        with advisory_lock(lock_id) as acquired:
            if not acquired:
                raise Exception('Lock not acquired')
            yield

    @contextlib.contextmanager
    def acquire_modify_queue_lock(self, stream):
        lock_id = f'queue-{stream.uuid}'
        with advisory_lock(lock_id) as acquired:
            if not acquired:
                raise Exception('Lock not acquired')
            yield

    @contextlib.contextmanager
    def acquire_manage_queue_intervals_lock(self, queue_uuid):
        lock_id = f'queue-interval-{queue_uuid}'
        with advisory_lock(lock_id) as acquired:
            if not acquired:
                raise Exception('Lock not acquired')
            yield

    def http_react_response(self, _type, payload):
        """
        SUCCESS
        """
        response = {
            "system": {
                "status": 200,
                "message": "Ok",
            },
            "redux": {
                "type": _type,
                "payload": payload,
            },
        }
        return JsonResponse(response)

    def http_response_200(self, data=None):
        """
        SUCCESS
        """
        response = {
            "system": {
                "status": 200,
                "message": "Ok",
            },
        }
        if data is not None:
            response["data"] = data
        if type(response) == dict:
            return JsonResponse(response)
        if type(response) == list:
            return JsonResponse(serialize("json", response), safe=False)
        return JsonResponse(serialize("json", [response])[1:-1], safe=False)

    def http_response_400(self, message):
        """
        BAD REQUEST
        """
        return JsonResponse(
            {
                "system": {
                    "status": 400,
                    "message": message,
                },
            },
            status=400,
        )

    def http_response_403(self, message):
        """
        FORBIDDEN
        """
        return HttpResponseForbidden(message)

    def http_response_422(self, message):
        '''
        INVALID FORMAT
        '''
        return HttpResponse(status_code=422, message=message)

    def template_response(self, request, template, context={}):
        return TemplateResponse(request, template, context)

    def redirect_response(self, redirect_path):
        return HttpResponseRedirect(redirect_path)
