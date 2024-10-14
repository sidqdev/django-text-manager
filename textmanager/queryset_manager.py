from typing import List, Union

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.db.models import Q

from textmanager.models import Language, Text, LanguageText


def _filter_languages(qs: QuerySet[Language], ids: Union[None, List[str]]) -> QuerySet[Language]:
    if ids is None:
        return qs
    
    return qs.filter(Q(alpha2__in=ids) | Q(alpha3_b__in=ids))
    
def available_languages_queryset_filter(qs: QuerySet[Language]) -> QuerySet[Language]:
    return _filter_languages(qs, settings.TEXT_MANAGER_AVAILABLE_LANGUAGES)

def extra_languages_queryset_filter(qs: QuerySet[Language], text: Text) -> QuerySet[Language]:
    excluded_languages = []
    if text is not None:
        excluded_languages = [x.language for x in LanguageText.objects.filter(text=text).all()]
    return _filter_languages(qs, settings.TEXT_MANAGER_EXTRA_LANGUAGES).exclude(id__in=[x.id for x in excluded_languages])

def available_for_user_text_queryset_filter(qs: QuerySet[Text], user: User) -> QuerySet[Text]:
    if user.is_superuser:
        return qs

    return qs.filter(Q(category__groups__in=user.groups.all()) | Q(category__groups=None))
