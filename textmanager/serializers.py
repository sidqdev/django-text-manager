from django.conf import settings
from rest_framework import serializers



class TextParamsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    unique_id = serializers.CharField(required=False)
    language = serializers.CharField(default=settings.TEXT_MANAGER_DEFAULT_API_LANGUAGE, allow_null=True)
    render_with_jinja = serializers.BooleanField(default=True)
    params = serializers.JSONField(default={})

    def validate(self, attrs):
        if 'id' not in attrs and 'unique_id' not in attrs:
            raise serializers.ValidationError({
                "id": ["id or unique_id is required"],
                "unique_id": ["id or unique_id is required"]
            })
        return super().validate(attrs)

class LanguageSerializer(serializers.Serializer):
    alpha2 = serializers.CharField()
    alpha3_b = serializers.CharField()
    english_name = serializers.CharField()
    language_name = serializers.CharField()
    flag = serializers.CharField()