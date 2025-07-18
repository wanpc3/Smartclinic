from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Medicine, UserMedicine

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter Username'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter Email'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter Password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password'
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your email'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password'
        })

class MedicineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter Medicine Name'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Enter Medicine Description'
        })
        self.fields['expiry_date'].widget.attrs.update({
            'placeholder': 'Enter Expiry Date'
        })
        self.fields['price'].widget.attrs.update({
            'placeholder': 'Enter Price'
        })
        
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'expiry_date', 'price']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'})
        }
        
class UserMedicineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserMedicineForm, self).__init__(*args, **kwargs)
        self.fields['dosage'].widget.attrs.update({
            'placeholder': 'Enter Dosage'
        })
        self.fields['frequency'].widget.attrs.update({
            'placeholder': 'Enter Frequency'
        })
        self.fields['start_date'].widget.attrs.update({
            'placeholder': 'Enter Start Date'
        })
        self.fields['end_date'].widget.attrs.update({
            'placeholder': 'Enter End Date'
        })
        self.fields['instructions'].widget.attrs.update({
            'placeholder': 'Enter Instructions (optional)',
            'rows': 3
        })

    class Meta:
        model = UserMedicine
        #fields = ['medicine', 'dosage', 'frequency', 'start_date', 'end_date', 'instructions']
        exclude = ['user', 'medicine']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }