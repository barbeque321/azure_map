from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader

# Create your views here.
def azure_map_project(request):
    return render(request, 'azure_map_project.html', {})

# def generate(request):
# # template = loader.get_template('azure_map_project.html')	
# location = request.GET.get('theAdress')
# # context = {
# #         'location': location,
# #     }
# # return HttpResponse(template.render(context, request))
# return render(request, 'azure_map_project.html', {'location': location})