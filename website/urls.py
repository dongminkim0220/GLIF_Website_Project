from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('setups.urls')),
    path('admin/', admin.site.urls),
    path('aboutus/introduction/', include('aboutus_introduction.urls')),
    path('aboutus/glifers/', include('aboutus_glifers.urls')),
    path('announcement/', include('announcement.urls')),
    path('daily/overview/', include('daily_overview.urls')),
    path('daily/newsclipping/', include('daily_news.urls')),
    path('daily/market/', include('daily_market.urls')),
    path('indepthanalysis', include('indepthanalysis.urls')),
    path('recruiting', include('recruiting.urls')),
]
