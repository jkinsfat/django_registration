from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^secrets', views.secrets),
    url(r'^secrets/', views.popular),
    url(r'^process/(?P<datatype>\w+)', views.process)
]
