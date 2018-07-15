from django.conf.urls import url

#imports from sorp_app
from . import views

app_name='sorp_app'
urlpatterns=[
      url(r'^$',views.domain_redirect,name='domain_redirect'),
      url(r'^login/$',views.user_login,name='user_login_page'),
      url(r'^profile/$', views.user_profile, name = 'user_profile_page'),
      url(r'^create_student/$',views.create_student,name='user_reg_output'),
      url(r'^deactivate/$',views.deactivate,name='user_reg_deactivate'),
      url(r'^success/$',views.reg_success,name='user_reg_success'),
      url(r'^upload_due/$',views.upload_due,name='upload_due'),
      url(r'^upload_sub/$',views.upload_sub,name='upload_sub'),
      url(r'^upload_result/',views.upload_result,name='upload_result'),
      url(r'^change_password/',views.change_password,name='password_change'),

  ]



