from django.shortcuts import render
from django.http import HttpResponse

from .forms import PatientForm, PrimaryDiagnoseForm

from .models import Patient

def create(request):
    if request.method == 'GET':
        patient = PatientForm()
        primary = PrimaryDiagnoseForm()
        context = {
        'patient': patient, 
        'primary': primary,
        }
        return render(request, 'patient/create.html', context)
    else:
        patient = PatientForm(request.POST)
        primary = PrimaryDiagnoseForm(request.POST)
        context = {
        'patient': patient, 
        'primary': primary,
        }
        return render(request, 'patient/create.html', context)