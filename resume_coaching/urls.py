from django.urls import include, path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='resume_coaching-index'),
    path('<int:pk>', PostDetailView.as_view(), name = "resume_coaching-detail"),
    path('new', PostCreateView.as_view(), name = "resume_coaching-new"),
    path('<int:pk>/update', PostUpdateView.as_view(), name = "resume_coaching-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = "resume_coaching-delete"),
]