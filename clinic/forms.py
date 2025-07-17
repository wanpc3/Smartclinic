from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Medicine, UserMedicine

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

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
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'expiry_date', 'price']
        
class UserMedicineForm(forms.ModelForm):
    class Meta:
        model = UserMedicine
        #fields = ['medicine', 'dosage', 'frequency', 'start_date', 'end_date', 'instructions']
        exclude = ['user', 'medicine']