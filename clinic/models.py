from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #username = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    #password = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class UserMedicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    instructions = models.TextField(blank=True, null=True)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

class Reminder(models.Model):
    user_medicine = models.ForeignKey(UserMedicine, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    is_taken = models.BooleanField(default=False)

class IntakeLog(models.Model):
    user_medicine = models.ForeignKey(UserMedicine, on_delete=models.CASCADE)
    intake_time = models.DateTimeField(auto_now_add=True)
    was_on_time = models.BooleanField()
    notes = models.TextField(blank=True, null=True)
