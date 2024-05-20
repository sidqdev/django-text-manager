from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.forms.models import BaseInlineFormSet
from textmanager.models import Language, Text, Category, LanguageText
from textmanager import queryset_manager


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('alpha2', 'alpha3_b', 'english_name', 'language_name', 'flag')
    search_fields = list_display

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return queryset_manager.available_languages_queryset_filter(super().get_queryset(request))


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'title')
    search_fields = list_display
    filter_horizontal = ('groups', )


class LanguageTextInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        qs = queryset_manager.extra_languages_queryset_filter(Language.objects)
        if qs is not None:
            kwargs['initial'] = [
                {'language': i}
                for i in qs
            ]
        super(LanguageTextInlineFormSet, self).__init__(*args, **kwargs)


class LanguageTextInline(admin.TabularInline):
    model = LanguageText
    autocomplete_fields = ('language',)
    formset = LanguageTextInlineFormSet

    def get_extra(self, request: HttpRequest, obj=None, **kwargs: Any) -> int:
        return queryset_manager.extra_languages_queryset_filter(Language.objects).count()


class TextAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'category', 'description')
    list_filter = ('category',)
    autocomplete_fields = ('category',)
    inlines = [LanguageTextInline,]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        return queryset_manager.available_for_user_text_queryset_filter(qs, request.user)


admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Text, TextAdmin)