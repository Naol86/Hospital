from django.urls import path
from . import views

urlpatterns = [
    path('register',views.RegisterPatient,name='Register-Patient'),
    path('nurse',views.Nurse,name='Nurse'),
]