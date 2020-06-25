from rest_framework.generics import ListAPIView, RetrieveAPIView

from home.models import Patient, Country, Region, District, Occupation
from .serializer import PatientSerializer, CountrySerializer, DistrictSerializer, OccupationSerializer

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
        districtId = self.kwargs['districtId']
        return District.objects.filter(region_id=districtId)


class OccupationListView(ListAPIView):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer