from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^login/$', views.logIn),
    url(r'^viewName/$', views.view_Name),
    url(r'^logout/$', views.logOut),

]