from django.shortcuts import redirect, render
from .forms import Patient_Form
from .models import Register_Patient

# Create your views here.

def Register_Patient(request):
    form = Patient_Form()
    if request.method == 'POST':
        form = Patient_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Register-Patient')
    context = { 'form' : form}
    return render(request,'register.html',context)

def Nurse(request):
    # patient data for nurses to view and manage patients
    patient = Register_Patient.objects.get(First_Name='Naol')
    
    context = {'patient' : patient}
    return render(request,'nurse.html',context)