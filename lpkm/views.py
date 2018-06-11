# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    #return(HttpResponse('hello {} '.format(name)))
    return render(request,"base.html")
def exemple(request):
	return render(request,"exempl.html")
def topics(request):
	return render(request,"topics.html")
def call_of_paper(request):
	return render(request,"call_of_paper.html")
def commettees(request):
	return render(request,"commettees.html")
def contact(request):
	return render(request,"contact.html")
def program(request):
	return render(request,"program.html")
def previous_lpkm(request):
	return render(request,"previous_lpkm.html")