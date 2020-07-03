from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User

from home.models import Patient, Country, Region, District, Occupation
from .serializer import PatientSerializer, CountrySerializer, DistrictSerializer, OccupationSerializer, UserSerializer


class PatientListView(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetialView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetialView(RetrieveAPIView):
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
    print(request.data)
    patient = PatientSerializer(data=request.data.get('patient'))
    if patient.is_valid():
        try:
            print(patient.data)
            obj = Patient.objects.get(id=request.data.get('patient').get('id'))
            print(obj)
            for key, value in request.data.get('patient').items():
                setattr(obj, key, value)
            obj.save(force_update=True)
        except Patient.DoesNotExist:
           Response(patient.data, status=status.HTTP_406_NOT_ACCEPTABLE) 
        return Response(patient.data, status=status.HTTP_200_OK)
    print(patient.errors)
    return Response(patient.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
def GetDistrictById(request, districtId):
    district = District.objects.get(id=districtId)
    if district:
        return Response(DistrictSerializer(district).data, status=status.HTTP_200_OK)
    return Response('Page not found', status=status.HTTP_404_NOT_FOUND)