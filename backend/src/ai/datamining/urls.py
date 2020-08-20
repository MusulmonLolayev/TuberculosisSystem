from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import RangeListView, UpdateAcceptableIntevals_as_View, GetRangesUpdatingStatus

urlpatterns = [
    
    # Get requests
    # GetAccetableIntervals
    path('getaccetableintervals', RangeListView.as_view()),
    path('updateaccetableintervals/<method>', UpdateAcceptableIntevals_as_View, name='updateaccetableintervals'),
    path('GetRangesUpdatingStatus', GetRangesUpdatingStatus, name='GetRangesUpdatingStatus'),

]

urlpatterns = format_suffix_patterns(urlpatterns)