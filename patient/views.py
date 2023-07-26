from django.shortcuts import redirect, render
from .forms import Patient_Form,Nurse_Form
from .models import Register_Patient
from django.db.models import Q

# Create your views here.
def Home(request):
    
    if request.GET.get('search') != None :
        search = request.GET.get('search')
    else:
        search = '#'
    
    patients = Register_Patient.objects.filter(
        Q(Full_Name__icontains = search) 
        )
    patient_count = patients.count()
    
    context = {'patients':patients}
    
    return render (request,"home.html",context)
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
    
    nurse = Nurse_Form()
    
    if request.method == 'POST':
        nurse = Nurse_Form(request.POST)
        if nurse.is_valid():
            nurse.save()
            return redirect('Nurse')
    # patients = Register_Patient.objects.filter(Nurse_Checked=False)
    
    context = {'nurse':nurse}
    return render(request,'nurse.html',context)