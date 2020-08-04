from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.staticfiles.storage import staticfiles_storage

import numpy as np

from sklearn.preprocessing import minmax_scale

import os

from ai.settings import DISCRIPTION_FEATURES, MODELS_NAMES

from ai.common.functions import AcceptableInterval, GetFeatures, GetAttributes_Names

@api_view(['GET'])
def GetAccetableIntervals(request, method):
    
    def query(item):
        if item['type'] in ['float', 'str']:
            return True
        return False

    f_nc = [] 
    f_c = []

    for model_item in MODELS_NAMES:
        item_nc, item_c = GetAttributes_Names(model_item, query)
        f_nc += item_nc
        f_c += item_c

    not_computing, computing = GetFeatures(query)

    X = np.array(computing)

    """path = staticfiles_storage.path('data/data.txt')
    
    X = np.loadtxt(path)

    #minmax_scale(X, copy=False)

    result = []

    for i in range(X.shape[1]):
        for j in range(i + 1, X.shape[1]):
            result.append(AcceptableInterval(X[:, i], X[:, j], method))"""

    return Response(X, status=status.HTTP_200_OK)