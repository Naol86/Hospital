from django.db import models
from birthday import BirthdayField,BirthdayManager

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
    Full_Name = models.CharField(max_length=200)
    Father_Name = models.CharField(max_length=150)
    Mother_Name = models.CharField(max_length=150)
    Age = models.IntegerField(default=0)
    Sex = models.CharField(max_length=10,choices=sex,default="None")
    Address = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=15)
    Emergency_Phone_Number = models.CharField(max_length=15)
    Birth_Day = models.DateField()
    
    Created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['Created_at']
        
    def __str__(self):
        """Unicode representation of Register_Patient."""
        name = self.First_Name + ' ' + self.Middle_Name + ' ' + self.Last_Name
        return name
    def save(self, *args, **kwargs):
        self.Full_Name = f"{self.First_Name} {self.Middle_Name} {self.Last_Name}"
        super(Register_Patient, self).save(*args, **kwargs)

class Doctors(models.Model):
    """Model definition for Doctors."""
    
    Name = models.CharField(max_length=100)
    Room = models.IntegerField(default=0)

    def __str__(self):
        """Unicode representation of Doctors."""
        return self.Name

class Nurse(models.Model):
    """Model definition for Nurse."""
    
    patient = models.ForeignKey(Register_Patient,on_delete=models.PROTECT)
    status = models.CharField(max_length=500)
    doctor = models.ForeignKey(Doctors,on_delete=models.PROTECT)
    
    def __str__(self):
        """Unicode representation of Nurse."""
        pass

