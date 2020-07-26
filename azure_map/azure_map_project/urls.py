from django.urls import path
from azure_map_project import views
from django.urls import include, path, re_path
from django.conf.urls import url



urlpatterns += [
    url('', azure_map_project.views.azure_map_project, name='azure_map_project'),
    url('', azure_map_project.views.generate, name='generate'),
]

app_name = 'azure_map_project'