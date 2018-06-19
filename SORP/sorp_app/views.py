from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from sorp_app import forms

#imports form sorp_app
from . import forms
from . import models

#for domain redirect
def domain_redirect(request) :
	return redirect('login/')

#function to find the group of user
def get_user_group(user):
	g_name = user.groups.values_list('name',flat=True)
	return g_name[0]


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
				return HttpResponseRedirect('/profile/')
			else:
				return HttpResponseRedirect('/login/')

	return render(request,'sorp_app/login.html', {'form':form})



#user_profile
@login_required
def user_profile(request):
	grp = get_user_group(request.user)
	iform = forms.StudentInfoForm()
	mform = forms.StudentMedicalForm()
	dobj = models.Documents.objects.all()
	print(dobj)

	if grp == 'Student':
		return render(request, 'sorp_app/s_profile.html')
	else:
		return render( request, 'sorp_app/r_addstudent.html', {'iform': iform , 'mform': mform, 'dobj': dobj})

