from django.urls import path

from .views import PatientListView, PatientDetialView

urlpatterns = [
    path('', PatientListView.as_view()),
    path('<pk>', PatientDetialView.as_view())
]