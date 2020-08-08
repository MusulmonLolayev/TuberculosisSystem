from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api_app.urls')),
    path('api/', include('ai.datamining.urls')),
    path('patient/', include('patientapp.urls')),
]
