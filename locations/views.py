from django.shortcuts import render
from .models import Location
# Create your views here.

def locationView(request):

    displyCountry = Location.objects.all()
    return render(request, 'location.html', {'Location':displyCountry})