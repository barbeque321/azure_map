from django.urls import path
from azure_map_project import views



app_name = 'azure_map'
urlpatterns = [
    path('', views.azure_map_project, name='azure_map_project'),
    # path('', views.current_datetime, name='current_datetime'),
]