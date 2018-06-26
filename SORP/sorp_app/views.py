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
    if grp == 'Student':
        user = request.user
        # user = User.objects.get(username = 'username')
        sobj = user.studentinfo
        return render(request, 'sorp_app/s_profile.html',{'sobj': sobj })

    elif grp == 'Registration Staff':
        iform = forms.StudentInfoForm()
        mform = forms.StudentMedicalForm()
        fform = forms.StudentFirstFeeForm()
        dobj = models.Documents.objects.all()
        return render( request, 'sorp_app/r_addstudent.html', {'iform': iform , 'mform': mform, 'dobj': dobj,'fform': fform })
    else:
        return HttpResponse("You are not student or a Registraion Staff")


#create_student user
@login_required
def create_student(request) :
    iform = forms.StudentInfoForm()
    mform = forms.StudentMedicalForm()
    fform = forms.StudentFirstFeeForm()

    if request.method == "POST":
        iform = forms.StudentInfoForm(request.POST)
        mform = forms.StudentMedicalForm(request.POST)
        fform = forms.StudentFirstFeeForm(request.POST)
        dobj = models.Documents.objects.all()

        if ( iform.is_valid() and mform.is_valid() and fform.is_valid()) is False :
            print(iform.errors.as_data())
            print(mform.errors.as_data())
            print(fform.errors.as_data())
            return render(request, 'sorp_app/r_addstudent.html',
                          {'iform': iform, 'mform': mform, 'dobj': dobj, 'fform': fform})
        else:
            iformm = iform.save(commit=False)
            mformm = mform.save(commit=False)
            fformm = fform.save(commit=False)
            #create user
            username = iform.cleaned_data['roll_no']
            password = iform.cleaned_data['father_name']
            email = iform.cleaned_data['email']
            user = User.objects.create_user(username = username, password = password, email = email)
            my_group = Group.objects.get(name='Student')
            my_group.user_set.add(user)
            #assgning OnetoOneField
            iformm.user = user
            iformm.save()
            mformm.student = iformm
            fformm.student = iformm
            mformm.save()
            fformm.save()

            #document assignment
            for i in range(1,dobj.count() + 1):
                strr =  "doc"+ str(i)
                sub = request.POST.get(strr)
                # print ("in i loop: ", i," strrr is ",sub,  type(sub), len(sub))
                if sub is not None :
                    ans = True if (sub == "Yes") else False
                    dinfo = models.DocumentInfo(student=iformm, document=dobj[i-1], submitted=ans)
                    dinfo.save()
            iform.save_m2m()

            return HttpResponse("Your request is POST")

    else:
        return render(request, 'sorp_app/r_addstudent.html',{'iform': iform, 'mform': mform, 'dobj': dobj, 'fform': fform})



#editing of student info
@login_required
def update_student(request) :
    if request.method == 'POST' :
        roll_no = request.POST['roll']
        obj = models.StudentInfo.get(roll_no=roll_no)
        iform = forms.StudentInfoForm(instanse=obj)
        mform = forms.StudentMedicalForm(instanse=obj)
        fform = forms.StudentFirstFeeForm(instance=obj)
        return render(request, 'sorp_app/r_addstudent.html',{'iform': iform, 'mform': mform, 'dobj': dobj, 'fform': fform})


#deactiviting of student
@login_required
def deactivate(request) :
    if request.method == 'POST' :
        roll_no = request.POST['roll']
        obj = models.StudentInfo.get(roll_no=roll_no)
        obj.roll_no = 'roll_no'+'D'
        obj.active_status = False
        return HttpResponse("STUDENT DEACTIVATED")




