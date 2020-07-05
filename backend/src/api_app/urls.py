from django.urls import path
from .views import PatientCreate

from rest_framework.urlpatterns import format_suffix_patterns

from .views import PatientListView, CountryListView, \
     RegionListView, DistrictListView, OccupationListView, \
         GetDistrictById, PatientEdit, DeletePatient, ClinicalFormListView, \
             LocalizationListView, PrevalenceListView, CharacterOfStoolListView, \
                 PrimaryDiagnoseListView, TakingMedicineListView, ComplaintListView, ImmunogramListView, OtherListView

urlpatterns = [
    
    # Get requests
    # /patients
    path('patients', PatientListView.as_view()),

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

    # /primarydiagnose/patientId
    path('primarydiagnose/<patientId>', PrimaryDiagnoseListView.as_view()),

    # /TakingMedicine/patientId
    path('TakingMedicine/<patientId>', TakingMedicineListView.as_view()),

    # /Complaint/patientId
    path('Complaint/<patientId>', ComplaintListView.as_view()),

    # /Immunogram/patientId
    path('Immunogram/<patientId>', ImmunogramListView.as_view()),

    # /other/patientId
    path('other/<patientId>', OtherListView.as_view()),

    # Post and delete requests
    # Create patient by Post request
    # /PatientCreate
    path('patientcreate', PatientCreate, name='patientcreate'),

    # Patient patient by Post request
    # /PatientEdit
    path('patientedit', PatientEdit, name='patientedit'),

    # Patient patient by Delete request
    # /DeletePatient
    path('patientdelete', DeletePatient, name='patientdelete'),

]

urlpatterns = format_suffix_patterns(urlpatterns)