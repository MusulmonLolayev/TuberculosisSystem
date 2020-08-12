from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from ai.settings import DISCRIPTION_FEATURES, MODELS_NAMES
from ai.common.functions import AcceptableInterval, GetFeatures, GetAttributes_Names, UpdateAcceptableIntevals
from ai.models import Range
from ai.serializer import RangeSerializer

class RangeListView(ListAPIView):
    serializer_class = RangeSerializer

    def get_queryset(self):
        update_number = Range.objects.last().udapte_number
        return Range.objects.filter(udapte_number=update_number)


@api_view(['GET'])
def UpdateAcceptableIntevals_as_View(request, method):
    try:
        UpdateAcceptableIntevals(method=method)
    except:
        return Response(status=500)
    return Response('Udated', status=200)