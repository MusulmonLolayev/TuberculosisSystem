from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from ai.settings import DISCRIPTION_FEATURES, MODELS_NAMES
from ai.common.functions import AcceptableInterval, GetFeatures, GetAttributes_Names, UpdateAcceptableIntevals
from ai.models import Range
from ai.serializer import RangeSerializer
from ai.settings import GLOBAL_UPDATINGS


class RangeListView(ListAPIView):
    serializer_class = RangeSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        update_number = Range.objects.last().udapte_number
        return Range.objects.filter(udapte_number=update_number)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetRangesUpdatingStatus(request):
    return Response(GLOBAL_UPDATINGS, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UpdateAcceptableIntevals_as_View(request, method):
    try:
        # Check there are any updating.
        if GLOBAL_UPDATINGS['hasUpdating'] and not GLOBAL_UPDATINGS['IsUpdatedRanges']:
            UpdateAcceptableIntevals(method=method)
            GLOBAL_UPDATINGS['IsUpdatedRanges'] = True
    except:
        return Response(status=500)
    return Response(GLOBAL_UPDATINGS, status=200)