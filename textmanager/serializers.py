from rest_framework import serializers
from textmanager import queryset_manager
from textmanager.models import Language


class TextParamsSerializer(serializers.Serializer):
    unique_id = serializers.CharField()
    language = serializers.CharField(required=False)
    render_with_jinja = serializers.BooleanField(default=True)
    params = serializers.JSONField()

    def validate_language(self, value: str):
        qs = queryset_manager.available_languages_queryset_filter(Language.objects)
        if not queryset_manager._filter_languages(qs, [value]).exists():
            raise serializers.ValidationError({"language": "available language not found"})
        
        return value
