from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient

def index(request):
    all_patient = Patient.objects.all()
    html = ''
    for item in all_patient:
        url = str(item.id)
        html += '<a href="' + url + '">' + str(item) + '</a> <br/>'
    return HttpResponse(html)
    
def detial(request, patient_id):
    return HttpResponse("<h1> Patient ID: " + str(patient_id) + "</h1>")
