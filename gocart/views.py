from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm
from django.http import HttpResponseForbidden

# -------------------------
# Authentication Views
# -------------------------

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'gocart/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == role:
            login(request, user)
            if not user.gender or not user.dob or not user.present_address:
                return redirect('complete_profile')
            return redirect('home')
    return render(request, 'gocart/login.html')



@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('confirm_logout')
    return render(request, 'gocart/logout_confirm.html')


def confirm_logout(request):
    logout(request)
    return redirect('home')
