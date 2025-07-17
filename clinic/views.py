from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import SignUpForm, SignInForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = SignInForm()
    
    return render(request, 'sign_in.html', {'form': form})

def sign_out(request):
    sign_out(request)
    return redirect('sign_in')

def dashboard(request):
    user_medicines = UserMedicine.objects.filter(user=request.user)
    return render(request, 'index.html', {'medicines': user_medicines})

def add_medicine(request):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        dosage = request.POST.get('dosage')
        frequency = request.POST.get('frequency')
        end_date = request.POST.get('end_date')
        
        medicine = Medicine.objects.create(
            name=medicine_name,
            dosage=dosage,
            frequency=frequency,
            end_date=end_date
        )
        
        UserMedicine.objects.create(user=request.user, medicine=medicine)
        return redirect('dashboard')
    
    return render(request, 'add_medicine.html')

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