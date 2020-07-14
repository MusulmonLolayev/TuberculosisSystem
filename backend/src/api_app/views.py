from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
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

class CharacterOfStoolListView(ListAPIView):
    queryset = CharacterOfStool.objects.all()
    serializer_class = CharacterOfStoolSerializer

class PrimaryDiagnoseListView(ListAPIView):
    serializer_class = PrimaryDiagnoseSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return PrimaryDiagnose.objects.filter(patient_id=patient_id)

class TakingMedicineListView(ListAPIView):
    serializer_class = TakingMedicineSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return TakingMedicine.objects.filter(patient_id=patient_id)

class ComplaintListView(ListAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return Complaint.objects.filter(patient_id=patient_id)

class BloodListView(ListAPIView):
    serializer_class = BloodAnalysisSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return BloodAnalysis.objects.filter(patient_id=patient_id)

class ImmunogramListView(ListAPIView):
    serializer_class = ImmunogramSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return Immunogram.objects.filter(patient_id=patient_id)

class OtherListView(ListAPIView):
    serializer_class = OtherSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return Other.objects.filter(patient_id=patient_id)

@api_view(['GET'])
def GetDistrictById(request, districtId):
    district = District.objects.get(id=districtId)
    if district:
        return Response(DistrictSerializer(district).data, status=status.HTTP_200_OK)
    return Response('Page not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def patient_request(request):
    try:
        # Get list of data
        if request.method == 'GET':
            return Response(PatientSerializer(Patient.objects.filter(status=True).order_by('-id', ), many=True).data, status=200)
        
        # Create object
        if request.method == 'POST':
            serializer = PatientSerializer(data=request.data.get('patient'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            patient = Patient.objects.get(id=request.data.get('patient').get('id'))
        except Patient.DoesNotExist:
            return Response(status=404)

        # Update object
        if request.method == 'PUT':
            serializer = PatientSerializer(patient, data=request.data.get('patient'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            patient.status = False
            patient.save()
            return Response('Deleted', status=200)
    except:
        Response(status=500)

@api_view(['POST', 'DELETE', 'PUT'])
def primary_request(request):
    try:
        # Create object
        if request.method == 'POST':
            serializer = PrimaryDiagnoseSerializer(data=request.data.get('primarydiagnose'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            primarydiagnose = PrimaryDiagnose.objects.get(id=request.data.get('primarydiagnose').get('id'))
        except PrimaryDiagnose.DoesNotExist:
            return Response(status=404)
        
        # Update object
        if request.method == 'PUT':
            #print(request.data)
            serializer = PrimaryDiagnoseSerializer(primarydiagnose, data=request.data.get('primarydiagnose'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        else:
            primarydiagnose.delete()
            return Response(status=200)
    except:
        return Response(status=500)

@api_view(['POST', 'DELETE', 'PUT'])
def taking_request(request):
    try:
        # Create object
        if request.method == 'POST':
            serializer = TakingMedicineSerializer(data=request.data.get('takingmedicine'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            takingmedicine = TakingMedicine.objects.get(id=request.data.get('takingmedicine').get('id'))
        except TakingMedicine.DoesNotExist:
            return Response(status=404)
        
        # Update object
        if request.method == 'PUT':
            #print(request.data)
            serializer = TakingMedicineSerializer(takingmedicine, data=request.data.get('takingmedicine'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            takingmedicine.delete()
            return Response(status=200)
    except:
        Response(status=500)

@api_view(['POST', 'DELETE', 'PUT'])
def complaint_request(request):
    try:        
        # Create object
        if request.method == 'POST':
            serializer = ComplaintSerializer(data=request.data.get('complaint'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            complaint = Complaint.objects.get(id=request.data.get('complaint').get('id'))
        except Complaint.DoesNotExist:
            return Response(status=404)
        
        # Update object
        if request.method == 'PUT':
            #print(request.data)
            serializer = ComplaintSerializer(complaint, data=request.data.get('complaint'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            complaint.delete()
            return Response(status=200)
    except:
        Response(status=500)

@api_view(['POST', 'DELETE', 'PUT'])
def blood_request(request):
    try:
        # Create object
        if request.method == 'POST':
            serializer = BloodAnalysisSerializer(data=request.data.get('bloodanalysis'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            bloodanalysis = BloodAnalysis.objects.get(id=request.data.get('bloodanalysis').get('id'))
        except BloodAnalysis.DoesNotExist:
            return Response(status=404)
        
        # Update object
        if request.method == 'PUT':
            #print(request.data)
            serializer = BloodAnalysisSerializer(bloodanalysis, data=request.data.get('bloodanalysis'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            complaint.delete()
            return Response(status=200)
    except:
        Response(status=500)

@api_view(['POST', 'DELETE', 'PUT'])
def immunogram_request(request):
    try:
        # Create object
        if request.method == 'POST':
            serializer = ImmunogramSerializer(data=request.data.get('immunogram'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            immunogram = Immunogram.objects.get(id=request.data.get('immunogram').get('id'))
        except Immunogram.DoesNotExist:
            return Response(status=404)
        
        # Update object
        if request.method == 'PUT':
            #print(request.data)
            serializer = ImmunogramSerializer(immunogram, data=request.data.get('immunogram'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            immunogram.delete()
            return Response(status=200)
    except:
        Response(status=500)

@api_view(['POST', 'DELETE', 'PUT'])
def other_request(request):
    try:
        # Create object
        if request.method == 'POST':
            serializer = OtherSerializer(data=request.data.get('other'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            other = Other.objects.get(id=request.data.get('other').get('id'))
        except Other.DoesNotExist:
            return Response(status=404)
        
        # Update object
        if request.method == 'PUT':
            #print(request.data)
            serializer = OtherSerializer(other, data=request.data.get('other'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            other.delete()
            return Response(status=200)
    except:
        Response(status=500)