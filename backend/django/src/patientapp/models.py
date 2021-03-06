from django.db import models
import datetime


class Country(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
        
class District(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name

class Occupation(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Patient(models.Model):
    number = models.IntegerField()
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    birthday = models.DateField(default=datetime.date.today)
    fromdate = models.DateField(default=datetime.date.today)
    district = models.ForeignKey(District, on_delete = models.CASCADE)
    address = models.TextField(default='')
    gender = models.BooleanField(default=True)
    occupation = models.ForeignKey(Occupation, on_delete = models.CASCADE)
    # it is extra field for patient to help not deleting
    status = models.BooleanField(default=True)

    """def save(self, **kwargs):
        super().save(**kwargs)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name

class ClinicalForm(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Локализация (список/нет) in Column K
class Localization(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Распространенность (список/нет) in Column L
class Prevalence(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PrimaryDiagnose(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinicalform = models.ForeignKey(ClinicalForm, on_delete=models.CASCADE)
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE)
    prevalence = models.ForeignKey(Prevalence, on_delete=models.CASCADE)
    #инфильтрация yes or no
    infiltration = models.BooleanField(default=False)
    #распад (да/нет)
    decay = models.BooleanField(default=False)
    #обсеменение (да/нет)
    seeding = models.BooleanField(default=False)
    #рассасывание (да/нет)
    resorption = models.BooleanField(default=False)
    #уплотнение (да/нет)
    compaction = models.BooleanField(default=False)
    #рубцевание (да/нет)
    scarring = models.BooleanField(default=False)
    #обызвествление (да/нет)
    calcification = models.BooleanField(default=False)
    # БК in column no. 21 of excell
    bk = models.BooleanField(default=False)

    # status for taking on computing
    status = models.BooleanField(default=True)
    # created date
    date = models.DateField(default=datetime.date.today)

class TakingMedicine(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    fromdate = models.DateField(default=datetime.date.today)
    #стрептомицин (да/нет)
    streptomycin = models.BooleanField(default=False)
    #рифампицин (да/нет)
    rifampicin = models.BooleanField(default=False)
    #изониазид (да/нет)
    isoniazid = models.BooleanField(default=False)
    #пиразинамид (да/нет)
    pyrazinamide = models.BooleanField(default=False)
    #этамбутол (да/нет)
    ethambutol = models.BooleanField(default=False)

    # status for taking on computing
    status = models.BooleanField(default=True)

    date = models.DateField(default=datetime.date.today)

# Характер стула (список) in Column AP
class CharacterOfStool(models.Model):
    name = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    #диарея (да/нет)
    diarrhea = models.BooleanField(default=False)
    #нормальный стул  (да/нет)
    normal_stool = models.BooleanField(default=False)
    #запоры (да/нет)
    constipation = models.BooleanField(default=False)
    #Метеоризм  (да/нет)
    flatulence = models.BooleanField(default=False)
    #Боли в животе (да/нет)
    stomachache = models.BooleanField(default=False)

    #Частота стула
    from_stool_frequency = models.IntegerField(default=0)
    to_stool_frequency = models.IntegerField(default=0)
    character = models.ForeignKey(CharacterOfStool, on_delete=models.CASCADE)

    # status for taking on computing
    status = models.BooleanField(default=True)
    date = models.DateField(default=datetime.date.today)

class BloodAnalysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # эр
    er = models.FloatField(default=0)
    # лейк
    leyk = models.FloatField(default=0)
    # Hb
    hb = models.FloatField(default=0)
    # Цв.
    color = models.FloatField(default=0)
    # П/я
    pya = models.FloatField(default=0)
    # С/я
    sya = models.FloatField(default=0)
    # эоз
    eoz = models.FloatField(default=0)
    # Лф
    lf = models.FloatField(default=0)
    # мон
    mon = models.FloatField(default=0)
    # СОЭ
    coe = models.FloatField(default=0)

    act = models.FloatField(default=0)
    # ALT
    alt = models.FloatField(default=0)

    # status for taking on computing
    status = models.BooleanField(default=True)

    date = models.DateField(default=datetime.date.today)


class Other(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # Переносимость противотуберкулезной терапии (удовлетворительная, не удовлетворительная)
    # satisfactory or not satisfactory
    tuberculosis_tolerance = models.BooleanField(default=False)

    # Сопутствующее заболевания (наменование заболевания / нет)
    related_disease = models.BooleanField(default=False)
    # Тошнота (да/нет)
    nausea = models.BooleanField(default=False)
    # Рвота (да/нет)
    vomiting = models.BooleanField(default=False)
    # Головная боль (да/нет)
    headache = models.BooleanField(default=False)
    # Потливость (время дня)
    sweating = models.BooleanField(default=False)
    # Слабость (да/нет)
    weakness = models.BooleanField(default=False)
    # Аллергодерматозы (да/нет)
    allergodermatosis = models.BooleanField(default=False)
    # Потеря массы тела (интервал)
    from_weight_loss = models.FloatField(default=0)
    to_weight_loss = models.FloatField(default=0)

    # Копроскопия (да/нет)
    coproscopy = models.BooleanField(default=False)

    # status for taking on computing
    status = models.BooleanField(default=True)
    date = models.DateField(default=datetime.date.today)

class QuestionTitle(models.Model):
    name = models.CharField(default='', max_length=100)
    title = models.TextField(max_length=250, default='')
    isMany = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_title = models.ForeignKey(QuestionTitle, on_delete=models.PROTECT)
    text = models.TextField()
    point = models.IntegerField(default=1)
    weight = models.FloatField(default=1)
    
    def __str__(self):
        return self.text

class InitialQuestion(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.PROTECT)
    questions = models.CharField(blank=True, max_length=200)

    # status for taking on computing
    status = models.BooleanField(default=True)
    date = models.DateField(default=datetime.date.today)