from django.forms.models import BaseInlineFormSet
from textmanager.models import Language
from textmanager import queryset_manager


def language_text_inlile_formset_factory(text):
    class LanguageTextInlineFormSet(BaseInlineFormSet):
        def __init__(self, *args, **kwargs):
            qs = queryset_manager.extra_languages_queryset_filter(Language.objects, text)
            if qs is not None:
                kwargs['initial'] = [
                    {'language': i}
                    for i in qs
                ]
            super(LanguageTextInlineFormSet, self).__init__(*args, **kwargs)
    
    return LanguageTextInlineFormSet