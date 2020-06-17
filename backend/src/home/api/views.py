from rest_framework.generics import ListAPIView, RetrieveAPIView

from home.models import Patient
from .serializer import PatientSerializer

class PatientListView(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetialView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
