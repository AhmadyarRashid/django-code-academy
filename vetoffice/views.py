from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404

pets = [
  { "petname": "Fido", "animal_type": "dog"},
  { "petname": "Clementine", "animal_type": "cat"},
  { "petname": "Cleo", "animal_type": "cat"},
  { "petname": "Oreo", "animal_type": "dog"},
]

# Create your views here.
def home(request):
    try:
        found_pet = Patient.objects.get(pk=4)
    except Patient.DoesNotExist:
        raise Http404()
    context = {"name": "Djangoer", "pets": pets}
    return render(request, 'vetoffice/home.html', context)

class OwnerCreate(CreateView):
    model = Owner
    template_name = "vetoffice/owner_create_form.html"
    fields = ["first_name", "last_name", "phone"]

class OwnerUpdate(UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    fields = ["first_name", "last_name", "phone"]

class OwnerList(ListView):
    model = Owner
    template_name = "vetoffice/owner_list.html"

class OwnerDelete(DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"

class PatientCreate(CreateView):
    model = Patient
    template_name = "vetoffice/patient_create_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class PatientUpdate(UpdateView):
    model = Patient
    template_name = "vetoffice/patient_update_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class PatientList(ListView):
    model = Patient
    template_name = "vetoffice/patient_list.html"

class PatientDelete(DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"