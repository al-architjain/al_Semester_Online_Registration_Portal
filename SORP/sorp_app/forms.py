from django import forms
from sorp_app import models

#form for login purpose
class login_form(forms.Form):
    username = forms.CharField(label="Username ", widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"username" }), max_length=10)
    password = forms.CharField(label="Password ", widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password" }))

class StudentInfoForm(forms.ModelForm) :
    class Meta:
        model = models.StudentInfo
        exclude = ['user','img','year_of_admission','active_status','ug_sem', 'stud_doc']

class StudentMedicalForm(forms.ModelForm) :
    class Meta :
        model = models.StudentMedicalInfo
        exclude = ['student',]

class StudentFirstFeeForm(forms.ModelForm) :
    class Meta :
        model = models.StudentFirstFeeStatus
        exclude = ['student', ]
