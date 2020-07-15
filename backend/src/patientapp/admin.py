from django.contrib import admin
from .models import Country, Question, Region, Patient, District, Occupation, \
    ClinicalForm, Localization, Prevalence, CharacterOfStool, PrimaryDiagnose, \
        TakingMedicine, QuestionTitle

admin.site.register(Country)
admin.site.register(Question)
admin.site.register(QuestionTitle)
admin.site.register(Region)
admin.site.register(Patient)
admin.site.register(District)
admin.site.register(Occupation)
admin.site.register(ClinicalForm)
admin.site.register(Localization)
admin.site.register(Prevalence)
admin.site.register(CharacterOfStool)
admin.site.register(PrimaryDiagnose)
admin.site.register(TakingMedicine)
