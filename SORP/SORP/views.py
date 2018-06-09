#imports from django libraries
from django.conf.urls import url
from django.shortcuts import redirect


def domain_redirect(request) :
	return redirect('/login/')





