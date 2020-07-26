from django.urls import path
from azure_map_project import views
from django.urls import include, path, re_path
from django.conf.urls import url



urlpatterns = [
    path('', views.azure_map_project, name='my_map'),
    # url('', views.generate, name='generate'),
]

# app_name = 'azure_map_project'