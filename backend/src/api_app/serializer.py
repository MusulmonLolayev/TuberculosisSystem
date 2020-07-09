from rest_framework import serializers

from patientapp.models import Patient, District, Region, Country, Occupation, \
    ClinicalForm, Localization, Prevalence, PrimaryDiagnose, TakingMedicine, \
    CharacterOfStool, Complaint, BloodAnalysis, Immunogram, Other

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
    """def save(self, *args, **kwargs):
        return super(Patient, self).save(*args, **kwargs)"""
    
    def update_as_SQL(self, id):
        data = self.data
        query = "UPDATE patientapp_patient SET number={0}, last_name='{1}', " + \
            "first_name='{2}', middle_name='{3}', birthday='{4}', address='{5}', " + \
                "fromdate='{6}', gender={7}, district_id={8}, occupation_id={9}, status={10} WHERE id={11}"
        query = query.format(
            data.get('number'),
            data.get('last_name'),
            data.get('first_name'),
            data.get('middle_name'),
            data.get('birthday'),
            data.get('address'),
            data.get('fromdate'),
            data.get('gender'),
            data.get('district'),
            data.get('occupation'),
            data.get('status'),
            id
            )
        print(query)

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