from django.urls import include, path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='announcement-index'),
    path('<int:pk>', PostDetailView.as_view(), name = "announcement-detail"),
    path('new', PostCreateView.as_view(), name = "announcement-new"),
    path('<int:pk>/update', PostUpdateView.as_view(), name = "announcement-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = "announcement-delete"),
    path('<int:pk>/download', views.download),
]
