from django.urls import include, path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='resume_coaching-index'),
    path('<int:pk>', PostDetailView.as_view(), name = "resume_coaching-detail"),
    path('new', PostCreateView.as_view(), name = "resume_coaching-new"),
    path('<int:pk>/update', PostUpdateView.as_view(), name = "resume_coaching-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = "resume_coaching-delete"),
    path('<int:pk>/download', views.download),
    path('<int:pk>/comment/new', views.add_comment_to_post, name='add_comment_to_post'),
    path('<int:pk>/comment/<int:pk_comment>/edit', views.edit_comment_to_post, name='edit_comment_to_post'),
    path('<int:pk>/comment/<int:pk_comment>/delete', views.delete_comment_to_post, name='delete_comment_to_post'),


]