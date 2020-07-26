from django.urls import path
from azure_map_project import views
from django.urls import include, path, re_path, url


app_name = 'azure_map'
urlpatterns = [
    path('', views.azure_map_project, name='azure_map_project'),
    url('', views.generate, name='generate'),
    # path('', views.current_datetime, name='current_datetime'),
]