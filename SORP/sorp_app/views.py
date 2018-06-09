from django.shortcuts import render

# Create your views here.


def user_login_page(request) :
	return render(request,'sorp_app/login.html')