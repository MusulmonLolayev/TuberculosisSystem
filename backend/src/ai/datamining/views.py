from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.staticfiles.storage import staticfiles_storage

import numpy as np

from sklearn.preprocessing import minmax_scale

import os

def AcceptableInterval(x, y, method='mean'):

    value_x = None
    value_y = None

    if method == 'mean':
        value_x = x.mean()
        value_y = y.mean()
    else:
        value_x = np.median(x)
        value_y = np.median(y)

    R = x / value_x - y / value_y

    return R.argmin(), R.argmax()

@api_view(['GET'])
def GetAccetableIntervals(request, method):
    
    path = staticfiles_storage.path('data/data.txt')
    
    X = np.loadtxt(path)

    minmax_scale(X, copy=False)

    result = []

    for i in range(X.shape[1]):
        for j in range(i + 1, X.shape[1]):
            result.append(AcceptableInterval(X[:, i], X[:, j], method))

    return Response(result, status=status.HTTP_200_OK)