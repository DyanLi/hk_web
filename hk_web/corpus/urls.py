#coding utf-8

from django.conf.urls import include, url

from django.contrib import admin

from . import views
from . import lotusview

urlpatterns = [
    url(r'^$', views.intro),
    url(r'^intro$', views.intro, name="intro"),
    url(r'^contact$', views.contact, name="contact"),
    url(r'^abbreviation$', views.abbreviation, name="abbreviation"),
    url(r'^download$', views.download, name="download"),
    url(r'^history$', views.history, name="history"),
    
    # 妙法蓮華經
    url(r'^lotus/$', lotusview.lotus_index, name="lotus_index"),
    url(r'^lotus/intro$', lotusview.lotus_intro, name="lotus_intro"),
    url(r'^lotus/list$', lotusview.lotus_list, name="lotus_list"),
    url(r'^lotus/view/([-0-9]+)$', lotusview.lotus_view, name="lotus_view"),
    url(r'^lotus/go$', lotusview.lotus_go, name="lotus_go")
]