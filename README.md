## django-text-manager - no more problems with texts for bots, websites, etc.

#### v0.1 - Basic functionality
#### TODO - api support
## Documentation
### settings.py
```python3
INSTALLED_APPS = [
    ...
    "textmanager",
    ...
]

TEXT_MANAGER_EXTRA_LANGUAGES = ['uk'] # Optional, default languages when u add new text
TEXT_MANAGER_AVAILABLE_LANGUAGES = ['ru', 'uk', 'en'] # Optional, list of availbale languages in project 
```
### How to add languages? (load in database 107 different languages)
```bash
python3 manage.py migrate
python3 manage.py loadlanguages
```
### Usage
```python3
from textmanager.models import Text

text = Text.objects.get(unique_id='test').render(language="en", params={
    "var1": "friend"
})
print(text)

# >>> Hello, friend! - text in db: Hello, {{ var1 }}!
```
