from django.urls import path
from azure_map_project import views
from django.urls import include, path, re_path
from django.conf.urls import url



urlpatterns += [
    url('', views.azure_map_project, name='azure_map_project'),
    url('', views.generate, name='generate'),
]

app_name = 'azure_map_project'