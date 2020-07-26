from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url




urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # url('azure_map_project/', include('azure_map_project.urls', namespace="azure_map_project") ),
    path('azure_map_project/', include(("azure_map_project.urls", 'azure_map_project'), namespace="azure_map_project")),
]
