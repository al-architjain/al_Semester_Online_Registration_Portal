from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
# imports form sorp_app
from . import forms
from . import models
#for excel files.
import openpyxl

#-----------------------------------------------------------#

# for domain redirect
def domain_redirect(request):
    return redirect('login/')

# function to find the group of user
def get_user_group(user):
    g_name = user.groups.values_list('name', flat=True)
    return g_name[0]




# User Login Authetication
def user_login(request):
    form = forms.login_form()
    logout(request)

    if request.method == "POST":
        form = forms.login_form(request.POST)
        username = password = ''

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if (user is not None) and (user.is_active) :
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                return render(request, 'sorp_app/login.html', {'form': form, 'invalid':True})

    return render(request, 'sorp_app/login.html', {'form': form, 'invalid': False})


# user_profile
@login_required
def user_profile(request):
    grp = get_user_group(request.user)
    if grp == 'Student':
        user = request.user
        sobj = user.studentinfo
        dobj = models.DocumentInfo.objects.filter(student=sobj, submitted=False)
        subobj = models.Subjects.objects.filter(classname=sobj.ug_class, branch=sobj.ug_branch, semester=sobj.ug_sem)
        return render(request, 'sorp_app/stu_profile.html', {'sobj': sobj, 'dobj': dobj, 'subobj': subobj})

    elif grp == 'Registration Staff':
        uobj = request.user
        return render(request, 'sorp_app/reg_profile.html',{'uobj': uobj})


    elif grp == 'Librarian' or grp == 'Hostel Warden' or grp == 'Administration Block':
        uobj = request.user
        return render(request, 'sorp_app/staff_profile.html', {'uobj': uobj, 'ugrp': grp})

    else:
        return HttpResponse("You are not RegistrationStaff, Student, Librarian, Hostel Warden, Administration Block Staff.")


# create_student user
@login_required
def create_student(request):
    iform = forms.StudentInfoForm()
    # mform = forms.StudentMedicalForm()
    fform = forms.StudentFirstFeeForm()
    dobj = models.Documents.objects.all()
    if request.method == "POST":
        iform = forms.StudentInfoForm(request.POST)
        # mform = forms.StudentMedicalForm(request.POST)
        fform = forms.StudentFirstFeeForm(request.POST)

        if (iform.is_valid() and fform.is_valid()) is False:
            print(iform.errors.as_data())
            # print(mform.errors.as_data())
            print(fform.errors.as_data())
            return render(request, 'sorp_app/reg_addstudent.html',
                          {'iform': iform, 'dobj': dobj, 'fform': fform})
        else:
            iformm = iform.save(commit=False)
            fformm = fform.save(commit=False)

            # create user
            username = iform.cleaned_data['roll_no']
            password = iform.cleaned_data['father_name']
            email = iform.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email)

            # assigning group
            my_group = Group.objects.get(name='Student')
            my_group.user_set.add(user)

            # assgning OnetoOneField and saving
            iformm.user = user
            iformm.save()
            fformm.student = iformm
            fformm.save()

            # document assignment
            for i in range(1, dobj.count() + 1):
                strr = "doc" + str(i)
                submit = request.POST.get(strr)
                if submit is not None:
                    ans = True if (submit == "Yes") else False
                    dinfo = models.DocumentInfo(student=iformm, document=dobj[i - 1], submitted=ans)
                    dinfo.save()

            # saving multiple field.
            iform.save_m2m()

            return render(request, 'sorp_app/reg_success.html', {'username':username, 'password':password})

    else:
        return render(request, 'sorp_app/reg_addstudent.html',
                      {'iform': iform, 'dobj': dobj, 'fform': fform})


# editing of student info
@login_required
def update_student(request):
    if request.method == 'POST':
        roll_no = request.POST['roll']
        obj = models.StudentInfo.get(roll_no=roll_no)
        iform = forms.StudentInfoForm(instanse=obj)
        # mform = forms.StudentMedicalForm(instanse=obj)
        fform = forms.StudentFirstFeeForm(instance=obj)
        return render(request, 'sorp_app/reg_addstudent.html',
                      {'iform': iform, 'mform': mform, 'dobj': dobj, 'fform': fform})



# deactiviting of student
@login_required
def deactivate(request):
    if request.method == 'GET':
        return redirect('/profile/')
    if request.method == 'POST':
        #to free the allotted roll_no in student_info table
        roll_no = request.POST['d_roll_no']
        stu_info_obj = models.StudentInfo.objects.get(roll_no=roll_no)
        stu_info_obj.roll_no = roll_no + 'D'
        stu_info_obj.active_status = False
        stu_info_obj.save()

        # so the person cannot login() and allotted username(roll_no) is freed
        user = User.objects.get(username=roll_no)
        user.is_active = False
        user.username  = roll_no + 'D'
        user.save()

        return HttpResponse("STUDENT DEACTIVATED")



def reg_success(request):
    return render(request, 'sorp_app/reg_success.html')

# uploaded
def uploaded(request):
    if request.method == "POST":
        grp = get_user_group(request.user)
        path=request.FILES['file']

        wb_obj = openpyxl.load_workbook(path)
        sheet_obj = wb_obj.active

        rows = sheet_obj.max_row
        column = sheet_obj.max_column
        i = 2
        print(rows)
        while i <= rows:
            roll_obj = sheet_obj.cell(row=i, column=1).value
            fee_obj = sheet_obj.cell(row=i, column=2).value

            print("IT IS ROLL NO.")
            print(roll_obj)
            try:
                obj1 = models.StudentInfo.objects.get(roll_no=roll_obj)
                obj  = models.Due.objects.get(roll_no=obj1)
            # except models.StudentInfo.DoesNOTExist:
            #     return redirect('/profile/')
                # HttpResponse('some roll no. in file  does not exist')
            except models.Due.DoesNotExist:
                if grp == 'Librarian':
                    obj2 = models.Due(roll_no=obj1, library_due=fee_obj)
                elif grp == 'Administration Block':
                    obj2 = models.Due(roll_no=obj1, academic_due=fee_obj)
                else:
                    obj2 = models.Due(roll_no=obj1, hostel_due=fee_obj)
                obj2.save()
            else:
                if grp == 'Librarian':
                    obj.library_due=fee_obj
                elif grp == 'Administration Block':
                    obj.academic_due=fee_obj
                else:
                    obj.hostel_due=fee_obj
                obj.save()
            i=i+1
            print(i)
    return redirect('/profile/')

