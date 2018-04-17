"""Docstring."""
from django.conf.urls import url

from app import views

app_name = 'app'
urlpatterns = [
    url(r'^upload/?$', views.upload_sketch, name='upload_sketch'),
    url(r'^execute/?$', views.execute, name='execute'),

]
