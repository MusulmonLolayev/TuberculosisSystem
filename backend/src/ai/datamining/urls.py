from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import RangeListView, UpdateAcceptableIntevals_as_View

urlpatterns = [
    
    # Get requests
    # GetAccetableIntervals
    path('getaccetableintervals', RangeListView.as_view()),
    #path('getaccetableintervals/<method>', GetAccetableIntervals, name='getaccetableintervals'),
    path('updateaccetableintervals/<method>', UpdateAcceptableIntevals_as_View, name='updateaccetableintervals'),

]

urlpatterns = format_suffix_patterns(urlpatterns)