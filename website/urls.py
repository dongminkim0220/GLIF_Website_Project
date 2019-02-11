from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from users.views import glifers, applicants

urlpatterns = [
    # Home : Main View 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Auth setups
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', TemplateView.as_view(template_name="signup.html"), name='signup'),
    path('accounts/signup/glifer/', glifers.GliferSignUpView.as_view(), name='glifer_signup'),
    path('accounts/signup/applicant/', applicants.ApplicantSignUpView.as_view(), name='applicant_signup'),
    path('accounts/glifer/userinfo/<int:pk>', glifers.GliferEditView.as_view(), name = 'glifer_edit'),
    path('accounts/applicant/userinfo/<int:pk>', applicants.ApplicantEditView.as_view(), name = 'applicant_edit'),

    

    # Links setups
    path('aboutus/introduction/', include('aboutus_introduction.urls')),
    path('aboutus/glifers/', include('aboutus_glifers.urls')),
    path('notice/', include('announcement.urls'), name = "announcement"),
    path('daily/overview/', include('daily_overview.urls')),
    path('daily/newsclipping/', include('daily_news.urls')),
    path('daily/market/', include('daily_market.urls')),
    path('indepthanalysis/', include('indepthanalysis.urls')),
    path('recruiting/', include('recruiting.urls')),
    path('gliferonly/form_archive/', include('form_archive.urls')),
    path('gliferonly/resume_coaching/', include('resume_coaching.urls')),

    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

