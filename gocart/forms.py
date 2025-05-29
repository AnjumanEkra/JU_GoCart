# gocart/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

# ✅ Register Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'gender', 'dob',
            'present_address', 'postal_code', 'home_district',
            'nationality', 'phone', 'profile_picture'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

# ✅ Driver Extra Profile Form
class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'dob', 'present_address', 'postal_code',
            'home_district', 'nationality', 'phone', 'nid_card_no', 'profile_picture'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

# ✅ Custom Password Change Form (Optional: for better UI later)
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
