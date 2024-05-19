import os
import json
from django.core.management.base import BaseCommand
from textmanager.models import Language


class Command(BaseCommand):
    help = "Load language list to database"

    def handle(self, *args, **options):
        with open(f'{os.path.dirname(os.path.realpath(__file__))}/languages.json', 'r') as f:
            languages = json.load(f)
            for language in languages:
                try:
                    Language(**language).save()
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Error with load "{language}", exception: {e}')
                    )
        
        self.stdout.write(
            self.style.SUCCESS(f'{len(languages)} languages loaded')
        )
