from django import forms
from sorp_app import models

#form for login purpose
class login_form(forms.Form):
    username = forms.CharField(label="Username ", widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"username" }), max_length=10)
    password = forms.CharField(label="Password ", widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password" }))

class StudentInfoForm(forms.ModelForm) :
    class Meta:
        model = models.StudentInfo
        fields = '__all__'

class StudentMedicalForm(forms.ModelForm) :
    class Meta :
        model = models.StudentMedicalInfo
        fields = '__all__'

class StudentFirstFeeForm(forms.ModelForm) :
    class Meta :
        model = models.StudentFirstFeeStatus
        fields = '__all__'
