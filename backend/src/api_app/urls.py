from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

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
    # /primary_request/
    path('primary_request/<patient_id>', PrimaryDiagnoseListView.as_view()),

    # /TakingMedicine/patientId
    path('taking_request', taking_request),
    path('taking_request/<patient_id>', TakingMedicineListView.as_view()),

    # /Complaint
    path('complaint_request', complaint_request),
    path('complaint_request/<patient_id>', ComplaintListView.as_view()),

    # /Blood
    path('blood_request', blood_request),
    path('blood_request/<patient_id>', BloodListView.as_view()),

    # /Immunogram
    path('immunogram_request', immunogram_request),
    path('immunogram_request/<patient_id>', ImmunogramListView.as_view()),

    # /other
    path('other_request', other_request),
    path('other_request/<patient_id>', OtherListView.as_view()),

    # /Questions
    path('question_request', question_request),
    path('question_request/<question_title_id>', QuestionListView.as_view()),

    # /Question title
    path('question_titles', QuestionTitleListView.as_view()),
    path('question_title_request', question_title_request),
]

urlpatterns = format_suffix_patterns(urlpatterns)