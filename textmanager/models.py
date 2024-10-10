from typing import Union, List, Tuple

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import Group

import jinja2


class Language(models.Model):
    alpha2 = models.CharField(max_length=2, unique=True)
    alpha3_b = models.CharField(max_length=3, unique=True)
    english_name = models.CharField(max_length=30, unique=True)
    language_name = models.CharField(max_length=30, unique=True)
    flag = models.CharField(max_length=10)

    def __str__(self) -> int:
        return f"{self.english_name}{self.flag}"

    class Meta:
        db_table = 'textmanager_language'
    
    
class Category(models.Model):
    unique_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)

    groups = models.ManyToManyField(to=Group, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'categories'
        db_table = 'textmanager_category'        


class Text(models.Model):
    unique_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def render(self, language: Union[str, Language, None], params: dict, render_with_jinja=True) -> Union[str, List[Tuple[str, str]]]:
        if isinstance(language, str):
            language = Language.objects.filter(Q(alpha2=language) | Q(alpha3_b=language)).first()
        if not isinstance(language, Language):
            language = None
        
        if language is not None:
            language_text = LanguageText.objects.filter(language=language, text=self).first()
            if language_text is not None:
                return language_text.render(params=params, render_with_jinja=render_with_jinja)
            return None
        
        texts = list()
        for language_text in LanguageText.objects.filter(text=self).all():
            texts.append((
                language_text.language, language_text.render(params=params, render_with_jinja=render_with_jinja)
            ))
        
        return texts
    
    def __str__(self) -> str:
        return f"Text({self.unique_id})"

    class Meta:
        db_table = 'textmanager_text'


class LanguageText(models.Model):
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    text = models.ForeignKey(to=Text, on_delete=models.CASCADE)

    value = models.TextField()

    def render(self, params: dict, render_with_jinja=True):
        if render_with_jinja:
            return jinja2.Template(self.value).render(**params)
        return self.value

    class Meta:
        unique_together = ('language', 'text',)
        db_table = 'textmanager_language_text'