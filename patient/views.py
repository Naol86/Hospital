from django.shortcuts import redirect, render
from .forms import Patient_Form
from .models import RegisterPatient

# Create your views here.

def RegisterPatient(request):
    form = Patient_Form()
    if request.method == 'POST':
        form = Patient_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Register-Patient')
    context = { 'form' : form}
    return render(request,'register.html',context)

def Nurse(request):
    
    patient = RegisterPatient.objects.all()
    
    context = {'patient' : patient}
    return render(request,'nurse.html',context)