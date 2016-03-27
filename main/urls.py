from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^presentation', views.presentation, name='presentation'),
    url(r'^education', views.education, name='education'),
    url(r'^tarifs', views.tarifs, name='tarifs'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^accueil', views.accueil, name='accueil'),
]