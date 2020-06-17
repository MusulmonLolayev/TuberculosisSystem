from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('home/<int:patient_id>/', views.detial, name='detial'),
]
