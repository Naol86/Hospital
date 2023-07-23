from django.shortcuts import render
from .forms import Patient_Form
# Create your views here.
def Register_Patient(request):
    form = Patient_Form()
    context = { 'form' : form} 
    return render(request,'register.html',context)