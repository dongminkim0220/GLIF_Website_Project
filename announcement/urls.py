from django.urls import include, path
from django.contrib import admin
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
]