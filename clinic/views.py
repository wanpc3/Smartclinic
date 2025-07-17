from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import SignUpForm, SignInForm, MedicineForm, UserMedicineForm

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
        med_form = MedicineForm(request.POST)
        user_med_form = UserMedicineForm(request.POST)
        if med_form.is_valid() and user_med_form.is_valid():
            medicine = med_form.save()
            user_medicine = user_med_form.save(commit=False)
            user_medicine.user = request.user
            user_medicine.medicine = medicine
            user_medicine.save()
            return redirect('dashboard')
    else:
        med_form = MedicineForm()
        user_med_form = UserMedicineForm()

    return render(request, 'add_medicine.html', {
        'med_form': med_form,
        'user_med_form': user_med_form
    })

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