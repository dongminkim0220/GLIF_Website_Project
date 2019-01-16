from django.urls import include, path
from django.contrib import admin
from . import views
from .views import GliferList

urlpatterns = [
    path('<nth>', GliferList.as_view()),
]


