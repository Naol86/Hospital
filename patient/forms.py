from django.forms import ModelForm
from .models import Register_Patient,Nurse

class Patient_Form(ModelForm):
    
    class Meta:
        model = Register_Patient
        exclude = ["Full_Name"]
        
class Nurse_Form(ModelForm):
    
    class Meta:
        model = Nurse
        fields = "__all__" 