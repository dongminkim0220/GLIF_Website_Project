from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^introduction', views.introduction, name= 'introduction'),
    url(r'^announcement', views.announcement, name= 'announcement'),
    url(r'^daily', views.daily, name= 'daily'), 
    url(r'^inDepthAnalysis', views.inDepthAnalysis, name= 'inDepthAnalysis'), 
    url(r'^recruiting', views.recruiting, name= 'recruiting'), 
]