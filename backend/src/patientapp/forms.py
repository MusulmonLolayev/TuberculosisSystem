from django.forms import ModelForm, DateInput

from .models import Patient, PrimaryDiagnose

class PatientForm(ModelForm):
    
    required_css_class = "field"
    error_css_class = "error"
    
    class Meta:
        model = Patient
        fields = '__all__'
        
        widgets = {
            'birthday': DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'style':'width:170px'}),
            'fromdate': DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'style':'width:170px'}),
        }

class PrimaryDiagnoseForm(ModelForm):
    class Meta:
        model = PrimaryDiagnose
        exclude = ['patient']
        widgets = {
            'date': DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }