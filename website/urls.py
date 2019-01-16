from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home : Main View 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Auth setups
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    

    # Links setups
    path('aboutus/introduction/', include('aboutus_introduction.urls')),
    path('aboutus/glifers/', include('aboutus_glifers.urls')),
    path('announcement/', include('announcement.urls')),
    path('daily/overview/', include('daily_overview.urls')),
    path('daily/newsclipping/', include('daily_news.urls')),
    path('daily/market/', include('daily_market.urls')),
    path('indepthanalysis', include('indepthanalysis.urls')),
    path('recruiting', include('recruiting.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
