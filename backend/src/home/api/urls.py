from django.urls import path
from .views import PatientCreate

from rest_framework.urlpatterns import format_suffix_patterns

from .views import PatientListView, PatientDetialView, CountryListView, \
 CountryDetialView, RegionListView, DistrictListView, OccupationListView, \
 GetDistrictById, PatientEdit

urlpatterns = [
    # /patients
    path('patients', PatientListView.as_view()),
    # /patients/1
    path('patients/<pk>', PatientDetialView.as_view()),

    # /countries
    path('countries', CountryListView.as_view()),
    # /countries/1
    path('countries/<pk>', CountryDetialView.as_view()),

    # /regions_by_country/countryId
    path('regions_by_country/<countryId>', RegionListView.as_view()),

    # /districts_by_region/regionId
    path('districts_by_region/<regionId>', DistrictListView.as_view()),
    # /districts/districtId
    path('districts/<districtId>', GetDistrictById),

    # Occupation
    path('occupations', OccupationListView.as_view()),

    # Create patient by Post request
    # /PatientCreate
    path('patientcreate', PatientCreate, name='patientcreate'),

    # Patient patient by Post request
    # /PatientEdit
    path('patientedit', PatientEdit, name='patientedit'),
]

urlpatterns = format_suffix_patterns(urlpatterns)