from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

#imports form sorp_app
from . import forms

#function to find the group of user
def get_user_group(user):
	g_name = user.groups.values_list('name',flat=True)
	return g_name


#render login page
def user_login(request) :
	form = forms.login_form()

	if request.method == "POST":
		form = forms.login_form(request.POST)

		username = password = ''

		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect('profile/')
			else:
				return HttpResponseRedirect('/login/')

	return render(request,'sorp_app/login.html', {'form':form})



#user_profile
def user_profile(request):
	return HttpResponse("<h2>You are logged IN!</h2>")




#authenticate and check who the user is!
"""
def checking(request) :
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request,username=username, password=password)
	if user is not None :
		login(request,user)
		return HttpResponseRedirect('/main/')
	else :
		return HttpResponse('/login/')
"""

# #rendering pages to different users
# @login_required(login_url='/login/')
# def profile(request) :
# 	user_group = request.user.groups.

