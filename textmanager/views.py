import json
from django.http import HttpRequest, JsonResponse

from rest_framework.views import APIView
from rest_framework import permissions

from textmanager.serializers import TextParamsSerializer
from textmanager.models import Language, Text


class TextView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: HttpRequest):
        data = TextParamsSerializer(data=json.loads(request.body))
        if not data.is_valid():
            return JsonResponse(data.errors)
        

    # TODO: api for getting text