from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='recruiting-index'),
    path('new', views.index, name = "recruiting-new")
]