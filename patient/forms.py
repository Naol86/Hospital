from django.forms import ModelForm
from .models import Register_Patient

class Patient_Form(ModelForm):
    
    class Meta:
        model = Register_Patient
        fields = '__all__'