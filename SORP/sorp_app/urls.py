from django.conf.urls import url

#imports from sorp_app
from . import views 

urlpatterns=[
      url(r'^$',views.user_login_page,name='user_login_page')
  
]

#hello

