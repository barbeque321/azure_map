from django.urls import path
from azure_map_project.views import show_map
from django.urls import include, path, re_path
from django.conf.urls import url



urlpatterns = [
    path('', views.show_map, name='my_map'),
    # url('', views.generate, name='generate'),
]

app_name = 'azure_map_project'