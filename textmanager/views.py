import json
from django.http import HttpRequest, JsonResponse

from rest_framework.views import APIView
from rest_framework import permissions

from textmanager.serializers import TextParamsSerializer, LanguageSerializer
from textmanager.models import Language, Text
from textmanager import queryset_manager, responses


class TextView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: HttpRequest):
        data = TextParamsSerializer(data=json.loads(request.body))
        if not data.is_valid():
            return JsonResponse(data.errors)
        
        language = data.validated_data['language']
        unique_id = data.validated_data['unique_id']
        render_with_jinja = data.validated_data['render_with_jinja']
        params = data.validated_data['params']

        if language is not None:
            qs = queryset_manager.available_languages_queryset_filter(Language.objects)
            language = queryset_manager._filter_languages(qs, [data.validated_data['language']]).first()
            if language is None:
                return responses.LANGUAGE_NOT_FOUND
        
        text = queryset_manager.available_for_user_text_queryset_filter(
            Text.objects, request.user
        ).filter(unique_id=unique_id).first()
        
        if text is None:
            return responses.TEXT_NOT_FOUND
        
        rendered_text = text.render(language=language, params=params, render_with_jinja=render_with_jinja)

        if rendered_text is None:
            return responses.TEXT_NOT_FOUND
        
        if not isinstance(rendered_text, list):
            return JsonResponse({"text": rendered_text})
        else:
            texts = [{
                "language": LanguageSerializer().to_representation(language),
                "text": text
            } for language, text in rendered_text]
            return JsonResponse({"texts": texts})