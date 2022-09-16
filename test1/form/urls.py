from django.urls import path
from . import views
urlpatterns = [
  path('', views.form, name='form'),
  path('create', views.create, name='create'),
  path('index', views.index, name='index')
]