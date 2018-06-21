from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group

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
	# print(dlist)
	if grp == 'Student':
		return render(request, 'sorp_app/s_profile.html')
	else:
		iform = forms.StudentInfoForm()
		mform = forms.StudentMedicalForm()
		fform = forms.StudentFirstFeeForm()
		dobj = models.Documents.objects.all()
		dlist = ["NA"] * (dobj.count() + 1)
		return render( request, 'sorp_app/r_addstudent.html', {'iform': iform , 'mform': mform, 'dobj': dobj,'fform': fform, 'dlist':dlist})

# def s_registered(request):
# 	if request.method=='POST':
# 		form = forms.StudentInfoForm(request.POST)
# 		print(form.name_eng)
# 		return HttpResponse("Suck sexl! ")
# 	else:
# 		return HttpResponse("Successfull! ")

#create_student user
@login_required
def create_student(request) :
    iform = forms.StudentInfoForm(request.POST)
    mform = forms.StudentMedicalForm(request.POST)
    fforms = forms.StudentFirstFeeForm(request.POST)
    if request.method = "POST" :
        if iform.is_valid() and mform.is_valid() and fforms.is_valid() :
            f = iform.save(commit=False)
            #create user
            username = iform.cleaned_data['roll_no']
            password = iform.cleaned_data['']
            email = iform.cleaned_data['email']
            user = User.objects.create_user(username = username, password = password, email = email)
            #assgning OnetoOneField
            f.user = user
            #document information
            dobj = request.POST['dobj']
            temp = len(dobj)
            for i in temp :
                if(dobj[i] is 'YES') :


    else :
        return HttpResponse("Request is  not POST")

