from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Register_Patient)
admin.site.register(models.Doctors)
admin.site.register(models.Nurse)
