from django.shortcuts import render
#from django.http import HttpResponse
from cars.models import Car
 

# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains = search)

    return render(
        request,
        'cars.html',
        {'cars': cars}
        )
    
 
def template_bootstrap(request):
    return render(
        request,
        'temp_bootstrap.html')