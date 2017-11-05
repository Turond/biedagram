from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.homepage, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', auth_views.login, {'template_name': 'gram/signin.html'}, name='signin'),
    url(r'^signout/$', auth_views.logout, {'template_name': 'gram/home.html'}, name='signout'),
]