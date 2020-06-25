from django.urls import path

from .views import PatientListView, PatientDetialView, CountryListView, \
 CountryDetialView, RegionListView, DistrictListView, OccupationListView

urlpatterns = [
    path('patients', PatientListView.as_view()),
    path('patients/<pk>', PatientDetialView.as_view()),

    path('countries', CountryListView.as_view()),
    path('countries/<pk>', CountryDetialView.as_view()),

    # /regions/countryId
    path('regions/<countryId>', RegionListView.as_view()),

    # /districts/districtId
    path('districts/<districtId>', DistrictListView.as_view()),

    # Occupation
    path('occupations', OccupationListView.as_view()),
]