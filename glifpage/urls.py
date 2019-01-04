from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^aboutus/introduction', views.aboutUs, name= 'introduction'),
    url(r'^aboutus/glifers', views.aboutUs, name= 'glifers'),
    url(r'^announcement', views.announcement, name= 'announcement'),
    url(r'^daily/overview', views.daily, name= 'overview'),
    url(r'^daily/news', views.daily, name= 'news'), 
    url(r'^daily/market', views.daily, name= 'market'), 
    url(r'^indepthanalysis', views.inDepthAnalysis, name= 'inDepthAnalysis'), 
    url(r'^recruiting', views.recruiting, name= 'recruiting'), 
    url(r'^gliferonly/review', views.gliferOnly, name= 'review'), 
    url(r'^gliferonly/admin', views.gliferOnly, name= 'admin'), 

]