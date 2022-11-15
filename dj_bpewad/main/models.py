from django.db import models

# Create your models here.

class Patients(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    dob = models.DateField()
    email = models.EmailField()
    #phone = models.CharField()      # There was an algorithm for this, CharField might not make sense here

class Doctors(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    email = models.EmailField()
    #phone = models.CharField()      # There was an algorithm for this, CharField might not make sense here

class History(models.Model):
    uname = models.CharField(max_length=30)
    time = models.DateTimeField()
    pressure = models.IntegerField()        # Might need to set min and max values, consult with team before migration