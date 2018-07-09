"""SORP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin

#imports from SORP
from SORP import views

from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/',   admin.site.urls),
    url(r'^', include('sorp_app.urls')),


    url(r'^pass_reset/', include('django.contrib.auth.urls')),
    url(r'^pass_reset/password_reset/$', auth_views.password_reset),
    url(r'^pass_reset/password_reset/done/$', auth_views.password_reset_done),
    url(r'^pass_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                auth_views.password_reset_confirm),
    url(r'^pass_reset/done/$', auth_views.password_reset_complete),
]

admin.site.site_title = "Admin"
admin.site.site_header = "NITH Registration administration"
admin.site.index_title = 'Index'
