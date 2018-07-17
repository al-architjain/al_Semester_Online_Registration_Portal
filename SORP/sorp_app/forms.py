from django import forms
from sorp_app import models

#form for login purpose
class login_form(forms.Form):
    username = forms.CharField(label="Username ", widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"username" }), max_length=32)
    password = forms.CharField(label="Password ", widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password" }),max_length=32)

class StudentInfoForm(forms.ModelForm) :
    # gender = forms.ChoiceField(
    #     widget = forms.Select(attrs = {'style': 'width: 100%'}),
    #     choices = models.StudentInfo.gender_choices
    # )
    #
    # religion = forms.ChoiceField(
    #     required = False,
    #     widget = forms.Select(attrs = {'style': 'width: 100%'}),
    #     choices = models.StudentInfo.religion_choices,
    # )
    #
    # area = forms.ChoiceField(
    #     required=False,
    #     widget=forms.Select(attrs={'style': 'width: 100%'}),
    #     choices=models.StudentInfo.area_choice,
    # )
    #
    # int_school_type = forms.ChoiceField(
    #     required=False,
    #     widget=forms.Select(attrs={'style': 'width: 100%'}),
    #     choices=models.StudentInfo.school_type_choices,
    # )
    #
    # int_school_area = forms.ChoiceField(
    #     required=False,
    #     widget=forms.Select(attrs={'style': 'width: 100%'}),
    #     choices=models.StudentInfo.area_choice,
    # )

    category_main = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%'}),
        queryset = models.Category.objects.all()
    )

    category_admission = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%'}),
        queryset = models.Category.objects.all()
    )

    int_school_board = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%'}),
        queryset=models.Board.objects.all()
    )

    ug_class = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%'}),
        queryset=models.UGClass.objects.all()
    )

    ug_branch = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%'}),
        queryset=models.UGBranch.objects.all()
    )

    class Meta:
        model = models.StudentInfo
        exclude = ['user','img','year_of_admission','date_of_admission','active_status','ug_sem', 'stud_doc']


class StudentFirstFeeForm(forms.ModelForm) :
    class Meta :
        model = models.StudentFirstFeeStatus
        exclude = ['student', ]





# Expired Classes:
#
# class StudentMedicalForm(forms.ModelForm) :
#     class Meta :
#         model = models.StudentMedicalInfo
#         exclude = ['student',]