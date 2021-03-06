from django.urls import include, path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='form_archive-index'),
    path('<int:pk>', PostDetailView.as_view(), name = "form_archive-detail"),
    path('new', PostCreateView.as_view(), name = "form_archive-new"),
    path('<int:pk>/update', PostUpdateView.as_view(), name = "form_archive-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = "form_archive-delete"),
    path('<int:pk>/download', views.download),
]