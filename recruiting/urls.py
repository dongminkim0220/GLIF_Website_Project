from django.urls import include, path
from django.contrib import admin
from . import views
from users.views.applicants import ApplicantListView, ApplicantDetailView

urlpatterns = [
    path('', views.index, name='recruiting-index'),
    path('list', ApplicantListView.as_view(), name = "applicant-list"),
    path('<int:pk>', ApplicantDetailView.as_view(), name = "applicant-detail"),
]