from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from patientapp.models import *

from .serializer import *

class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class RegionListView(ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        """
        This view should return a list of all the regions
        for the currently country.
        """
        countryId = self.kwargs['countryId']
        print('countryId', countryId)
        return Region.objects.filter(country_id=countryId)

class DistrictListView(ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        """
        This view should return a list of all the districts
        for the currently region.
        """
        regionId = self.kwargs['regionId']
        return District.objects.filter(region_id=regionId)

class OccupationListView(ListAPIView):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer

class ClinicalFormListView(ListAPIView):
    queryset = ClinicalForm.objects.all()
    serializer_class = ClinicalFormSerializer

class LocalizationListView(ListAPIView):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer

class PrevalenceListView(ListAPIView):
    queryset = Prevalence.objects.all()
    serializer_class = PrevalenceSerializer

class CharacterOfStoolListView(ListAPIView):
    queryset = CharacterOfStool.objects.all()
    serializer_class = CharacterOfStoolSerializer

class PrimaryDiagnoseListView(ListAPIView):
    serializer_class = PrimaryDiagnoseSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return PrimaryDiagnose.objects.filter(patient_id=patient_id)

class TakingMedicineListView(ListAPIView):
    serializer_class = TakingMedicineSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return TakingMedicine.objects.filter(patient_id=patient_id)

class ComplaintListView(ListAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return Complaint.objects.filter(patient_id=patient_id)

class BloodListView(ListAPIView):
    serializer_class = BloodAnalysisSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return BloodAnalysis.objects.filter(patient_id=patient_id)

class ImmunogramListView(ListAPIView):
    serializer_class = ImmunogramSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return Immunogram.objects.filter(patient_id=patient_id)

class OtherListView(ListAPIView):
    serializer_class = OtherSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return Other.objects.filter(patient_id=patient_id)

class QuestionTitleListView(ListAPIView):
    queryset = QuestionTitle.objects.all()
    serializer_class = QuestionTitleSerializer

class QuestionListView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class InitialQuestionListView(ListAPIView):
    serializer_class = InitialQuestionSerializer

    def get_queryset(self):

        patient_id = self.kwargs['patient_id']
        return InitialQuestion.objects.filter(patient_id=patient_id)

@api_view(['GET'])
def GetDistrictById(request, districtId):
    district = District.objects.get(id=districtId)
    if district:
        return Response(DistrictSerializer(district).data, status=status.HTTP_200_OK)
    return Response('Page not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def patient_request(request):
    try:
        # Get list of data
        if request.method == 'GET':
            return Response(PatientSerializer(Patient.objects.filter(status=True).order_by('-id', ), many=True).data, status=200)
        
        # Create object
        if request.method == 'POST':
            serializer = PatientSerializer(data=request.data.get('patient'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            patient = Patient.objects.get(id=request.data.get('patient').get('id'))
        except Patient.DoesNotExist:
            return Response(status=404)

        # Update object
        if request.method == 'PUT':
            serializer = PatientSerializer(patient, data=request.data.get('patient'))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            patient.status = False
            patient.save()
            return Response('Deleted', status=200)
    except:
        Response(status=500)

def general_request(request, ins_name, ins_class, ins_ser):
    try:
        # Create object
        if request.method == 'POST':
            print(request.data)
            serializer = ins_ser(data=request.data.get(ins_name))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data.get('id'), status=201)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=406)
        
        # find suitable instance
        try:
            instance = ins_class.objects.get(id=request.data.get(ins_name).get('id'))
        except ins_class.DoesNotExist:
            return Response(status=404)

        # Update object
        if request.method == 'PUT':
            serializer = ins_ser(instance, data=request.data.get(ins_name))
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=406)
        else:
            instance.delete()
            return Response('Deleted', status=200)
    except:
        Response(status=500)

@api_view(['POST', 'DELETE', 'PUT'])
def primary_request(request):
    return general_request(request, 'primarydiagnose', PrimaryDiagnose, PrimaryDiagnoseSerializer)

@api_view(['POST', 'DELETE', 'PUT'])
def taking_request(request):
    return general_request(request, 'takingmedicine', TakingMedicine, TakingMedicineSerializer)

@api_view(['POST', 'DELETE', 'PUT'])
def complaint_request(request):
    return general_request(request, 'complaint', Complaint, ComplaintSerializer)

@api_view(['POST', 'DELETE', 'PUT'])
def blood_request(request):
    return general_request(request, 'bloodanalysis', BloodAnalysis, BloodAnalysisSerializer)

@api_view(['POST', 'DELETE', 'PUT'])
def immunogram_request(request):
    return general_request(request, 'immunogram', Immunogram, ImmunogramSerializer)

@api_view(['POST', 'DELETE', 'PUT'])
def other_request(request):
    return general_request(request, 'other', Other, OtherSerializer)
    
@api_view(['POST', 'DELETE', 'PUT'])
def question_request(request):
    return general_request(request, 'question', Question, QuestionTitle)

@api_view(['POST', 'PUT', 'DELETE'])
def question_title_request(request):
    return general_request(request, 'question_title', QuestionTitle, QuestionTitleSerializer)

@api_view(['POST', 'PUT', 'DELETE'])
def initial_question_request(request):
    return general_request(request, 'initial_question', InitialQuestion, InitialQuestionSerializer)