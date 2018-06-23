from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
import json as simplejson
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
    if grp == 'Student':
        return render(request, 'sorp_app/s_profile.html')
    else:
        iform = forms.StudentInfoForm()
        mform = forms.StudentMedicalForm()
        fform = forms.StudentFirstFeeForm()
        dobj = models.Documents.objects.all()
        return render( request, 'sorp_app/r_addstudent.html', {'iform': iform , 'mform': mform, 'dobj': dobj,'fform': fform })



#create_student user
@login_required
def create_student(request) :
    iform = forms.StudentInfoForm(request.POST)
    mform = forms.StudentMedicalForm(request.POST)
    fform = forms.StudentFirstFeeForm(request.POST)
    dobj = models.Documents.objects.all()

    if request.method == "POST":
        if iform.is_valid() is False :
            print(iform.errors.as_data())
            return render(request, 'sorp_app/r_addstudent.html',
                          {'iform': iform, 'mform': mform, 'dobj': dobj, 'fform': fform})
        else:
            return HttpResponse("PASSED")

    else:
        return render( request, 'sorp_app/r_addstudent.html', {'iform': iform , 'mform': mform, 'dobj': dobj,'fform': fform })
    # if request.method == "POST" :
    #     #if iform.is_valid() and mform.is_valid() and fforms.is_valid() :
    #     f = iform.save(commit=False)
    #     #create user
    #     username = iform.cleaned_data['roll_no']
    #     password = iform.cleaned_data['father_name']
    #     email = iform.cleaned_data['email']
    #     user = User.objects.create_user(username = username, password = password, email = email)
    #     #assgning OnetoOneField
    #     f.user = user
    #     f.save()
    #     #document information
    #     temp = len(dlist)
    #     for i in range(temp) :
    #         if(dlist[i] is 'NA') :
    #             continue
    #         else:
    #             obj = models.Documents.objects.get(id=i)
    #             sub = True if (dlist[i] is 'YES') else False
    #             dinfo = models.DocumentInfo(student=f, document=obj, submitted=sub )
    #             dinfo.save()
    #     iform.save_m2m()
    #     return HttpResponse("Your request is POST")
    #     # else :
    #     #     return HttpResponse("FORM IS NOT VALID")
    # return 1render(request, 'sorp_app/r_addstudent.html',{'iform': iform, 'mform': mform, 'dobj': dobj, 'fform': fform})
    #
# for i in range(1,dobj.count() + 1):
#     strr =  "doc"+ str(i)
