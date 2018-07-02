from django.conf.urls import url

#imports from sorp_app
from . import views

urlpatterns=[
      url(r'^$',views.domain_redirect,name='domain_redirect'),
      url(r'^login/$',views.user_login,name='user_login_page'),
      url(r'^profile/$', views.user_profile, name = 'user_profile_page'),
      url(r'^create_student/$',views.create_student,name='user_reg_output'),
  ]



