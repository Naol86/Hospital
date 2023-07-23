from django.urls import path
from . import views

urlpatterns = [
    path('register',views.Register_Patient,name='Register-Patient'),
]