import numpy as np

from patientapp.models import Patient, PrimaryDiagnose, TakingMedicine, Complaint, BloodAnalysis, Immunogram, Other

from api_app.serializer import PatientSerializer, PrimaryDiagnoseSerializer, TakingMedicineSerializer, ComplaintSerializer, BloodAnalysisSerializer, ImmunogramSerializer, OtherSerializer


from ai.settings import DISCRIPTION_FEATURES

def GetAttributes(serializer, item, discription_name, query):
    nc = []
    c = []

    values = serializer(item).data
    discriptions = DISCRIPTION_FEATURES[discription_name]
        
    for item in discriptions:
        if query(item):
            if item['is_computing'] == True:
                c.append(values [item['feature']])
            if item['is_display'] == True:
                nc.append(values[item['feature']])
    return nc, c

def GetFeatures(query):
    not_computing=[]
    computing = []

    for index, item in enumerate(Patient.objects.filter(status=True)):
        row_nc = []
        row_c = []

        nc, c = GetAttributes(PatientSerializer, item, 'Patient', query)
        row_nc = row_nc + nc
        row_c = row_c + c

        primary = PrimaryDiagnose.objects.filter(patient=item.id, status=True).last()
        nc, c = GetAttributes(PrimaryDiagnoseSerializer, primary, 'PrimaryDiagnose', query)
        row_nc = row_nc + nc
        row_c = row_c + c

        taking = TakingMedicine.objects.filter(patient=item.id, status=True).last()
        nc, c = GetAttributes(TakingMedicineSerializer, taking, 'TakingMedicine', query)
        row_nc = row_nc + nc
        row_c = row_c + c

        complaint = Complaint.objects.filter(patient=item.id, status=True).last()
        nc, c = GetAttributes(ComplaintSerializer, complaint, 'Complaint', query)
        row_nc = row_nc + nc
        row_c = row_c + c

        blood = BloodAnalysis.objects.filter(patient=item.id, status=True).last()
        nc, c = GetAttributes(BloodAnalysisSerializer, blood, 'BloodAnalysis', query)
        row_nc = row_nc + nc
        row_c = row_c + c

        immunogram = Immunogram.objects.filter(patient=item.id, status=True).last()
        nc, c = GetAttributes(ImmunogramSerializer, immunogram, 'Immunogram', query)
        row_nc = row_nc + nc
        row_c = row_c + c

        other = Other.objects.filter(patient=item.id, status=True).last()
        nc, c = GetAttributes(OtherSerializer, other, 'Other', query)
        row_nc = row_nc + nc
        row_c = row_c + c

        computing.append(row_c)
        not_computing.append(row_nc)
    
    return not_computing, computing

def AcceptableInterval(x, y, method='mean'):

    value_x = None
    value_y = None

    if method == 'mean':
        value_x = x.mean()
        value_y = y.mean()
    else:
        value_x = np.median(x)
        value_y = np.median(y)

    R = x / value_x - y / value_y

    return R.argmin(), R.argmax()
