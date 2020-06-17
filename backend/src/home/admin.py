from django.contrib import admin
from .models import Country, Question, Region, Patient, District

admin.site.register(Country)
admin.site.register(Question)
admin.site.register(Region)
admin.site.register(Patient)
admin.site.register(District)