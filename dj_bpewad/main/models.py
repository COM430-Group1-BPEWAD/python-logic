from django.db import models

# Create your models here.

class Patient_Authentication(models.Model):
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Patient_Contact(models.Model):
    uname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    emergencyName = models.CharField(max_length=30)
    emergencyPhone = models.CharField(max_length=20)
    doctorName = models.CharField(max_length=30)
    doctorPhone = models.CharField(max_length=20)
    hospital= models.CharField(max_length=50)

class Health_History(models.Model):
    uname = models.CharField(max_length=30) 
    height = models.CharField(max_length=10)
    weight = models.IntegerField()
    currentMed = models.CharField(max_length=30)
    pastMed = models.CharField(max_length=30)

class Blood_Pressure_Log(models.Model):
    uname = models.CharField(max_length=30)
    time = models.DateTimeField()
    pressure = models.IntegerField()        # Might need to set min and max values, consult with team before migration

class BMI_Log(models.Model):
    uname = models.CharField(max_length=30)
    date = models.DateField()
    height = models.CharField(max_length=10)
    weight = models.IntegerField()
    BMI = models.DecimalField(max_digits=4, decimal_places=2)