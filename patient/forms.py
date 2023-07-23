from django.forms import ModelForm
from .models import RegisterPatient

class Patient_Form(ModelForm):
    
    class Meta:
        model = RegisterPatient
        fields = '__all__'