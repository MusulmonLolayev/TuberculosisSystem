from rest_framework import serializers

from patientapp.models import *

from django.contrib.auth.models import User

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = Region
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    class Meta:
        model = District
        fields = '__all__'

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    
    #id = serializers.IntegerField()
    #district = DistrictSerializer()
    #occupation = OccupationSerializer()
    
    class Meta:
        model = Patient
        fields = '__all__'

class ClinicalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalForm
        fields = '__all__'

class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = '__all__'

class PrevalenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prevalence
        fields = '__all__'

class PrimaryDiagnoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryDiagnose
        fields = '__all__'

class TakingMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakingMedicine
        fields = '__all__'

class CharacterOfStoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterOfStool
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'

class BloodAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodAnalysis
        fields = '__all__'

class ImmunogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immunogram
        fields = '__all__'

class OtherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Other
        fields = '__all__'

class QuestionTitleSerializer(serializers.ModelSerializer):
    #questions = serializers.SerializerMethodField()
    class Meta:
        model = QuestionTitle
        fields = '__all__'
    """def get_questions(self, obj):
        res = QuestionSerializer(Question.objects.filter(question_title_id=obj.id))
        print(res)
        return res"""

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'