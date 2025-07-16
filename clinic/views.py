from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .models import *
from .serializers import *

def clinic(request):
    template = loader.get_template('landingPage.html')
    return HttpResponse(template.render())

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class UserMedicineViewSet(viewsets.ModelViewSet):
    queryset = UserMedicine.objects.all()
    serializer_class = UserMedicineSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class IntakeLogViewSet(viewsets.ModelViewSet):
    queryset = IntakeLog.objects.all()
    serializer_class = IntakeLogSerializer