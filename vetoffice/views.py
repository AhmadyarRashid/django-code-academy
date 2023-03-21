from django.shortcuts import render, redirect
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from .forms import OwnerCreateForm

pets = [
  { "petname": "Fido", "animal_type": "dog"},
  { "petname": "Clementine", "animal_type": "cat"},
  { "petname": "Cleo", "animal_type": "cat"},
  { "petname": "Oreo", "animal_type": "dog"},
]

def logout_view(request):
    logout(request)
    return redirect("home")

# Create your views here.
@login_required
def home(request):
    # try:
    #     found_pet = Patient.objects.get(pk=4)
    # except Patient.DoesNotExist:
    #     raise Http404()
    context = {"name": "Djangoer", "pets": pets}
    return render(request, 'vetoffice/home.html', context)

# STEP 1
# class OwnerCreate(CreateView):
#     model = Owner
#     template_name = "vetoffice/owner_create_form.html"
#     fields = ["first_name", "last_name", "phone"]
#     OR
#     form_class = OwnerCreateForm

# STEP 1
@login_required
def OwnerCreate(request):
    if request.method == "POST":
        form = OwnerCreateForm(request.POST)
        if form.is_valid():
            form.same()
    else:
        form = OwnerCreateForm()
    return render(request, "vetoffice/owner_create_form.html", {"form":form})     

#  STEP 3
# def OwnerCreate(request):
#   if request.method == "POST":
#     newOwner = Owner()
#     newOwner.first_name = request.POST['first_name']
#     newOwner.last_name = request.POST['last_name']
#     newOwner.phone_number = request.POST['phone_number']
#     newOwner.save()

#   return render(request, "vetoffice/owner_create_form.html")   

class OwnerUpdate(LoginRequiredMixin, UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    fields = ["first_name", "last_name", "phone"]

class OwnerList(LoginRequiredMixin, ListView):
    model = Owner
    template_name = "vetoffice/owner_list.html"

class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"

class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "vetoffice/patient_create_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = "vetoffice/patient_update_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class PatientList(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "vetoffice/patient_list.html"

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"