from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.homepage, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', auth_views.login, {'template_name': 'gram/signin.html'}, name='signin'),
    url(r'^signout/$', auth_views.logout, {'template_name': 'gram/home.html'}, name='signout'),
    url(r'^upload/$', views.image_upload, name='image_upload'),
    url(r'^(?P<post_author>.+)/post/(?P<post_id>[0-9]+)/$', views.view_post, name='view_post'),
    url(r'^profile/(?P<post_author>.+)/$', views.view_profile, name='view_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)