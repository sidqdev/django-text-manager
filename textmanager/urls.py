from django.urls import path

from textmanager.views import TextView

urlpatterns = [
    path("text/", TextView.as_view()),
]
