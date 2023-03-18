from django.shortcuts import render
from .models import State, Attraction

# Create your views here.
def home(request):
    all_attractions = Attraction.objects.all()
    context = { "attractions": all_attractions }
    return render(request, "tourist_attractions/home.html", context)

def details(request, statename):
    attractions = Attraction.objects.all()
    context = { "attractions": attractions, "statename": statename.replace("-", "")}
    return render(request, "tourist_attractions/details.html", context)