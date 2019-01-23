from django.urls import include, path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CreateReport
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='daily_news-index'),
    path('<int:pk>', PostDetailView.as_view(), name = "daily_news-detail"),
    path('new', PostCreateView.as_view(), name = "daily_news-new"),
    path('<int:pk>/update', PostUpdateView.as_view(), name = "daily_news-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = "daily_news-delete"),
    # path('<int:pk>/create_report', views.createReport),
    path('<int:pk>/create_report', CreateReport.as_view(), name = "pdfcreate"),

]