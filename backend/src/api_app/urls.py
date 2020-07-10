from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CountryListView, primary_request, \
     RegionListView, DistrictListView, OccupationListView, \
         GetDistrictById, patient_request, ClinicalFormListView, \
             LocalizationListView, PrevalenceListView, CharacterOfStoolListView, \
                 taking_request, complaint_request, immunogram_request, other_request, blood_request

urlpatterns = [
    # /countries
    path('countries', CountryListView.as_view()),

    # /regions_by_country/countryId
    path('regions_by_country/<countryId>', RegionListView.as_view()),

    # /districts_by_region/regionId
    path('districts_by_region/<regionId>', DistrictListView.as_view()),
    # /districts/districtId
    path('districts/<districtId>', GetDistrictById),

    # Occupations
    path('occupations', OccupationListView.as_view()),

    # Clinical forms
    path('clinicalforms', ClinicalFormListView.as_view()),

    # Localization
    path('localization', LocalizationListView.as_view()),

    # Prevalence
    path('prevalence', PrevalenceListView.as_view()),

    # CharacterOfStoolListView
    path('characterofstool', CharacterOfStoolListView.as_view()),

    # Patient patient by Post request
    path('patient_request', patient_request),

    # /primary_request
    path('primary_request', primary_request),

    # /TakingMedicine/patientId
    path('taking_request', taking_request),

    # /Complaint
    path('complaint_request', complaint_request),

    # /Blood
    path('blood_request', blood_request),

    # /Immunogram
    path('immunogram_request', immunogram_request),

    # /other
    path('other_request', other_request),
]

urlpatterns = format_suffix_patterns(urlpatterns)