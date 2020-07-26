from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader

# Create your views here.
def azure_map_project(request):
    return render(request, 'azure_map_project.html', {})

def current_datetime(request):
    now = datetime.datetime.now()
    current_date = "<html><body>It is now %s.</body></html>" % now
    template = loader.get_template('azure_map_project.html')
    context = {
        'current_date': current_date,
    }
    return HttpResponse(template.render(context, request))


def generate(request):
template = loader.get_template('azure_map_project.html')	
location = request.GET.get('theAdress')
context = {
        'location': location,
    }
return HttpResponse(template.render(context, request))
# return render(request, 'azure_map_project.html', {'location': location})