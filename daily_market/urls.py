from django.urls import include, path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CreateReport

urlpatterns = [
    path('', PostListView.as_view(), name='daily_market-index'),
    path('<int:pk>', PostDetailView.as_view(), name = "daily_market-detail"),
    path('new', PostCreateView.as_view(), name = "daily_market-new"),
    path('<int:pk>/update', PostUpdateView.as_view(), name = "daily_market-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = "daily_market-delete"),
    path('<int:pk>/create_report', CreateReport.as_view(), name = "pdfcreate"),
]