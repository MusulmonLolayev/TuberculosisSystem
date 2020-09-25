from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('spa', views.spa, name='spa'),
]
