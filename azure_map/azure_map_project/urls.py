from django.urls import path
from azure_map_project import views

urlpatterns = [
    path('', views.azure_map_project, name='azure_map_project'),
]