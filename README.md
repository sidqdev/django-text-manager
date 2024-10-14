## django-text-manager - no more problems with texts for bots, websites, etc.

#### v0.1.1 - Basic functionality with api
#### v0.1.5 - Fixes of some bugs, new variable TEXT_MANAGER_DEFAULT_API_LANGUAGE in settings

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
TEXT_MANAGER_DEFAULT_API_LANGUAGE = 'en' # Optional, default language for api, fr. en to render english text if 'language' row in empty
TEXT_MANAGER_PERMISSION_CLASSES = ['rest_framework.permissions.IsAuthenticated',] # Optional, permission classes for api
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

## API
### urls.py
```python3
from django.urls import path, include

urlpatterns = [
    path("textmanager/", include("textmanager.urls")),
]
```
### how to send request?
```python3
import requests
import json
resp = requests.post(url="http://0.0.0.0:1234/textmanager/text/", json={
    "id": 5, # id or unique_id is required
    # or
    "unique_id": "test",

    "language": "en", # optional, default=None
    "render_with_jinja": False, # optional, default=true
    "params": {} # optional, default={}
}, headers={"Authorization": "Token ****"})
data = json.loads(resp.text)
print(data)

# >>> {'text': 'Hello, {{ var1 }}!'} # if language specified
# >>> {
#    'texts': [
#        {
#            'language': {
#                'alpha2': 'en', 
#                'alpha3_b': 'eng', 
#                'english_name': 'English', 
#                'language_name': 'English', 
#                'flag': '🇬🇧'
#            }, 
#            'text': 'Hello, {{ var1 }}!'
#        }, ...
#    ]
# }# if language is not specified
```
