from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.staticfiles.storage import staticfiles_storage

import numpy as np

from sklearn.preprocessing import minmax_scale

import os

from ai.settings import DISCRIPTION_FEATURES

from ai.common.functions import AcceptableInterval, GetFeatures

@api_view(['GET'])
def GetAccetableIntervals(request, method):
    
    def query(item):
        if item['type'] in ['float', 'str']:
            return True
        return False

    not_computing, computing = GetFeatures(query)

    data = np.array(computing)
    print(not_computing)
    print(data)

    path = staticfiles_storage.path('data/data.txt')
    
    X = np.loadtxt(path)

    minmax_scale(X, copy=False)

    result = []

    for i in range(X.shape[1]):
        for j in range(i + 1, X.shape[1]):
            result.append(AcceptableInterval(X[:, i], X[:, j], method))

    return Response(DISCRIPTION_FEATURES, status=status.HTTP_200_OK)