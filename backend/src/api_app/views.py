from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User

from patientapp.models import Patient, Country, Region, District, Occupation, ClinicalForm, \
    Localization, Prevalence, PrimaryDiagnose, TakingMedicine, CharacterOfStool, \
        Complaint, BloodAnalysis, Immunogram, Other

from .serializer import PatientSerializer, CountrySerializer, DistrictSerializer, \
    OccupationSerializer, ClinicalFormSerializer, LocalizationSerializer, PrevalenceSerializer, \
        PrimaryDiagnoseSerializer, TakingMedicineSerializer, CharacterOfStoolSerializer, \
            ComplaintSerializer, BloodAnalysisSerializer, ImmunogramSerializer, OtherSerializer

# Get requests of models or list views
class PatientListView(ListAPIView):
    queryset = Patient.objects.filter(status=True)
    serializer_class = PatientSerializer

class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class RegionListView(ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        """
        This view should return a list of all the regions
        for the currently country.
        """
        countryId = self.kwargs['countryId']
        print('countryId', countryId)
        return Region.objects.filter(country_id=countryId)

class DistrictListView(ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        """
        This view should return a list of all the districts
        for the currently region.
        """
        regionId = self.kwargs['regionId']
        return District.objects.filter(region_id=regionId)

class OccupationListView(ListAPIView):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer

class ClinicalFormListView(ListAPIView):
    queryset = ClinicalForm.objects.all()
    serializer_class = ClinicalFormSerializer

class LocalizationListView(ListAPIView):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer

class PrevalenceListView(ListAPIView):
    queryset = Prevalence.objects.all()
    serializer_class = PrevalenceSerializer

class PrimaryDiagnoseListView(ListAPIView):
    serializer_class = PrimaryDiagnoseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the primary diagnoses
        for the currently patient.
        """
        patientId = self.kwargs['patientId']
        return PrimaryDiagnose.objects.filter(patient_id=patientId)

class TakingMedicineListView(ListAPIView):
    serializer_class = TakingMedicineSerializer

    def get_queryset(self):
        """
        This view should return a list of all the taking medicine
        for the currently patient.
        """
        patientId = self.kwargs['patientId']
        return TakingMedicine.objects.filter(patient_id=patientId)

class CharacterOfStoolListView(ListAPIView):
    queryset = CharacterOfStool.objects.all()
    serializer_class = CharacterOfStoolSerializer

class ComplaintListView(ListAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        """
        This view should return a list of all the complaint
        for the currently patient.
        """
        patientId = self.kwargs['patientId']
        return Complaint.objects.filter(patient_id=patientId)

class BloodAnalysisListView(ListAPIView):
    serializer_class = BloodAnalysisSerializer

    def get_queryset(self):
        """
        This view should return a list of all the blood analysis
        for the currently patient.
        """
        patientId = self.kwargs['patientId']
        return BloodAnalysis.objects.filter(patient_id=patientId)

class ImmunogramListView(ListAPIView):
    serializer_class = ImmunogramSerializer

    def get_queryset(self):
        """
        This view should return a list of all the immunogram
        for the currently patient.
        """
        patientId = self.kwargs['patientId']
        return Immunogram.objects.filter(patient_id=patientId)

class OtherListView(ListAPIView):
    serializer_class = OtherSerializer

    serializer_class = ImmunogramSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Other
        for the currently patient.
        """
        patientId = self.kwargs['patientId']
        return Other.objects.filter(patient_id=patientId)

@api_view(['GET'])
def GetDistrictById(request, districtId):
    district = District.objects.get(id=districtId)
    if district:
        return Response(DistrictSerializer(district).data, status=status.HTTP_200_OK)
    return Response('Page not found', status=status.HTTP_404_NOT_FOUND)

# Patient's actions
@api_view(['POST'])
def PatientCreate(request):
    patient = PatientSerializer(data=request.data.get('patient'))
    if patient.is_valid():
        patient.save()
        return Response(patient.data, status=status.HTTP_201_CREATED)
    print(patient.errors)
    return Response(patient.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
def PatientEdit(request):
    patient = PatientSerializer(data=request.data.get('patient'))
    if patient.is_valid():
        try:

            patient = request.data.get('patient')


            obj = Patient.objects.get(id=request.data.get('patient').get('id'))
            
            obj.number = patient.get('number')
            obj.last_name = patient.get('last_name')
            obj.first_name = patient.get('first_name')
            obj.middle_name = patient.get('middle_name')
            obj.birthday = patient.get('birthday')
            obj.fromdate = patient.get('fromdate')
            obj.address = patient.get('address')
            obj.gender = patient.get('gender')
            obj.district =  District.objects.get(id=patient.get('district'))
            obj.occupation = Occupation.objects.get(id=patient.get('occupation'))
            
            obj.save(force_update=True)
        except Patient.DoesNotExist:
           Response(patient, status=status.HTTP_406_NOT_ACCEPTABLE) 
        return Response(patient, status=status.HTTP_200_OK)
    print(patient.errors)
    return Response(patient.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['DELETE'])
def DeletePatient(request):
    patient = PatientSerializer(data=request.data)
    if patient.is_valid():
        try:

            patient = request.data

            obj = Patient.objects.get(id=request.data.get('id'))

            obj.status = False

            obj.save(force_update=True)
        except Patient.DoesNotExist:
           Response(patient, status=status.HTTP_406_NOT_ACCEPTABLE) 
        return Response(patient, status=status.HTTP_200_OK)
    print(patient.errors)
    return Response(patient.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

