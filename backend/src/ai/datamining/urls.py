from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import GetAccetableIntervals

urlpatterns = [
    
    # Get requests
    # GetAccetableIntervals
    path('getaccetableintervals/<method>', GetAccetableIntervals, name='getaccetableintervals'),

]

urlpatterns = format_suffix_patterns(urlpatterns)