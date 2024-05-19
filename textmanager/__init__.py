from django.conf import settings

def configure_default_setting(default_settings: dict):
    for k, v in default_settings.items():
        try:
            getattr(settings, k)
        except:
            setattr(settings, k, v)


configure_default_setting({
    "TEXT_MANAGER_EXTRA_LANGUAGES": [], # In text admin extra inline items with languages
    "TEXT_MANAGER_AVAILABLE_LANGUAGES": None # For filtering in queryset in languages admin
})

if settings.TEXT_MANAGER_AVAILABLE_LANGUAGES is not None:
    settings.TEXT_MANAGER_EXTRA_LANGUAGES = list(set(settings.TEXT_MANAGER_EXTRA_LANGUAGES) & set(settings.TEXT_MANAGER_EXTRA_LANGUAGES))
