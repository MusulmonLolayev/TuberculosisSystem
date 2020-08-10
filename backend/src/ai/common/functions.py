import numpy as np

from patientapp.models import Patient, PrimaryDiagnose, TakingMedicine, Complaint, BloodAnalysis, Immunogram, Other

from api_app.serializer import PatientSerializer, PrimaryDiagnoseSerializer, TakingMedicineSerializer, ComplaintSerializer, BloodAnalysisSerializer, ImmunogramSerializer, OtherSerializer

from ai.settings import DISCRIPTION_FEATURES, MODELS_NAMES

from ai.models import Range

def GetAttributes_Names(discription_name, query):
    f_nc = []
    f_c = []

    discriptions = DISCRIPTION_FEATURES[discription_name]

    for item in discriptions:
        if query(item):
            if item['is_computing'] == True:
                f_c.append(item)
            else: 
                if item['is_display'] == True:
                    f_nc.append(item)

    return f_nc, f_c

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

    # if value some of them is zero, then must just send zeros as return values
    # That means, it is not neccessary on entry data.
    if value_x == 0 or value_y == 0:
        return 0, 0, 0, 0
    R = x / value_x - y / value_y

    return R.min(), R.max(), value_x, value_y

def UpdateAcceptableIntevals(method='mean'):
    # Getting names and values of features by calling GetFeatures
    def query(item):
            if item['type'] in ['float']:
                return True
            return False

    f_nc = [] 
    f_c = []

    for model_item in MODELS_NAMES:
        item_nc, item_c = GetAttributes_Names(model_item, query)
        f_nc += item_nc
        f_c += item_c
            
    not_computing, computing = GetFeatures(query)
    X = np.array(computing)

    update_number = Range.objects.last().udapte_number + 1

    for i in range(X.shape[0]):
        for j in range(i + 1, X.shape[0]):
            rng = Range()
            rng.udapte_number = update_number
            rng.feature_name1 = f_c[i]['feature']
            rng.feature_name2 = f_c[j]['feature']
            rng.l_R, rng.r_R, rng.sub_value1, rng.sub_value2 = AcceptableInterval(X[:, i], X[:, j], method=method)

            rng.save()
    pass