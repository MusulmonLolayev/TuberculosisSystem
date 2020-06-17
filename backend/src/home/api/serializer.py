from rest_framework import serializers

from home.models import Patient, District, Region, Country

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

class PatientSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'
