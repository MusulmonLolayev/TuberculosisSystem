from django.db import models
import datetime
from tuberculosis.settings import DATE_INPUT_FORMATS

class Question(models.Model):
    text = models.TextField()
    point = models.IntegerField()
    weight = models.FloatField()
    
    def __str__(self):
        return self.text;

class Country(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name;

class Region(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name;
        
class District(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name;

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name


    