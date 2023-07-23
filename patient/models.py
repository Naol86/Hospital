from django.db import models

# Create your models here.
sex = (
    ("Male","M"),
    ("Female","F"),
)
class Register_Patient(models.Model):
    """Model definition for Register_Patient."""

    First_Name = models.CharField(max_length=50)
    Middle_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Age = models.IntegerField(default=0)
    Sex = models.CharField(max_length=10,choices=sex,default="None")
    Address = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=15)
    Emergency_Phone_Number = models.CharField(max_length=15)
    Created_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Register_Patient."""

        verbose_name = 'Register_Patient'
        verbose_name_plural = 'Register_Patients'

    class Meta:
        ordering = ['Created_at']
        
    def __str__(self):
        """Unicode representation of Register_Patient."""
        name = self.First_Name + ' ' + self.Middle_Name + ' ' + self.Last_Name
        return name
    
class Nurse(models.Model):
    """Model definition for Nurse."""
    
    pass

    def __str__(self):
        """Unicode representation of Nurse."""
        pass

