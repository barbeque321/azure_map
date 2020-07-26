from django.shortcuts import render

# Create your views here.
def azure_map_project(request):
    return render(request, 'azure_map_project.html', {})

def generate(request):
location = request.GET.get('theAdress')

return render(request, 'azure_map_project.html', {'location': location})