from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^aboutus/introduction', views.aboutUs, name= 'introduction'),
    url(r'^aboutus/glifers', views.aboutUs, name= 'glifers'),
    url(r'^announcement', views.announcement, name= 'announcement'),
    url(r'^daily', views.daily, name= 'daily'), 
    url(r'^indepthanalysis', views.inDepthAnalysis, name= 'inDepthAnalysis'), 
    url(r'^recruiting', views.recruiting, name= 'recruiting'), 
]