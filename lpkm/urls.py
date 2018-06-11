"""ticsante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index/?$', views.index, name='index'),
	url(r'^exemple/?$', views.exemple, name='exemple'),
	url(r'^topics/?$', views.topics, name='topics'),
	url(r'^call_of_paper/?$', views.call_of_paper, name='call_of_paper'),
	url(r'^committees/?$', views.commettees, name='commettees'),
	url(r'^contact/?$', views.contact, name='contact'),
	url(r'^program/?$', views.program, name='program'),
	url(r'^previous_lpkm/?$', views.previous_lpkm, name='previous_lpkm'),
]
