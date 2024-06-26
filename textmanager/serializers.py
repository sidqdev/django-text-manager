from django.conf import settings
from rest_framework import serializers



class TextParamsSerializer(serializers.Serializer):
    unique_id = serializers.CharField()
    language = serializers.CharField(default=settings.TEXT_MANAGER_DEFAULT_API_LANGUAGE, allow_null=True)
    render_with_jinja = serializers.BooleanField(default=True)
    params = serializers.JSONField(default={})


class LanguageSerializer(serializers.Serializer):
    alpha2 = serializers.CharField()
    alpha3_b = serializers.CharField()
    english_name = serializers.CharField()
    language_name = serializers.CharField()
    flag = serializers.CharField()