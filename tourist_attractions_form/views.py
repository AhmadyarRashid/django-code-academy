from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import State, Attraction
from .forms import StateCreateForm, AttractionCreateForm

# Create your views here.
def home(request):
    all_attractions = Attraction.objects.all()
    context = { "attractions": all_attractions }
    return render(request, "tourist_attractions/home.html", context)

def details(request, statename):
    attractions = Attraction.objects.all()
    context = { "attractions": attractions, "statename": statename.replace("-", "")}
    return render(request, "tourist_attractions/details.html", context)

class StateCreate(CreateView):
    model = State
    form_class = StateCreateForm
    template_name = ""

class AttractionCreate(CreateView):
    model = Attraction
    form_class = AttractionCreateForm
    template_name = ""