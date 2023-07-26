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
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     # Check if the 'check_nurse' field is False
    #     check_nurse_value = self.Nurse.get('Check_Nurse') if self.instance else None

    #     if check_nurse_value is not None and not check_nurse_value:
    #         # If 'check_nurse' is False, exclude the 'batient' field
    #         self.fields.pop('patient')