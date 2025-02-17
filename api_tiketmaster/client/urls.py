from django.contrib import admin
from django.urls import path, include
from .views import events

urlpatterns = [
    path("events/", events, name="events"),
]