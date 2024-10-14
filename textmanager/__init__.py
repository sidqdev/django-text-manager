from django.conf import settings
from rest_framework import permissions


def configure_default_setting(default_settings: dict):
    for k, v in default_settings.items():
        try:
            getattr(settings, k)
        except:
            setattr(settings, k, v)

def import_by_path(name: str):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


configure_default_setting({
    "TEXT_MANAGER_EXTRA_LANGUAGES": [], # In text admin extra inline items with languages
    "TEXT_MANAGER_AVAILABLE_LANGUAGES": None, # For filtering in queryset in languages admin
    "TEXT_MANAGER_DEFAULT_API_LANGUAGE": None, # Default language for api, fr. en to render english text if 'language' row in empty
    "TEXT_MANAGER_PERMISSION_CLASSES": ['rest_framework.permissions.IsAuthenticated',],
})

if settings.TEXT_MANAGER_AVAILABLE_LANGUAGES is not None:
    settings.TEXT_MANAGER_EXTRA_LANGUAGES = list(set(settings.TEXT_MANAGER_EXTRA_LANGUAGES) & set(settings.TEXT_MANAGER_EXTRA_LANGUAGES))

settings.TEXT_MANAGER_PERMISSION_CLASSES = [import_by_path(x) for x in settings.TEXT_MANAGER_PERMISSION_CLASSES if isinstance(x, str)]
