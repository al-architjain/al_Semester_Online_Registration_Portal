from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

#imports form sorp_app
from . import forms

#render login page
def user_login_page(request) :
	form = forms.login_form()

	if request.method == "POST":
		form = forms.login_form(request.POST)

		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				return HttpResponse("User Exists :)")
			else:
				return HttpResponse("User doesnot exists")

	return render(request,'sorp_app/login.html', {'form':form})


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

