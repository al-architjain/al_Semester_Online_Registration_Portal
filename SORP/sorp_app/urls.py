from django.conf.urls import url

#imports from sorp_app
from . import views 

urlpatterns=[
      url(r'^$',views.user_login,name='user_login_page'),
      url(r'^profile/$', views.user_profile, name = 'user_profile_page')
      #url(r'^verify/',views.checking,name='checking')
  ]



