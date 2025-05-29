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

# -------------------------
# Profile Views
# -------------------------

@login_required
def complete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.gender = request.POST.get('gender')
        user.dob = request.POST.get('dob')
        user.present_address = request.POST.get('present_address')
        user.postal_code = request.POST.get('postal_code')
        user.home_district = request.POST.get('home_district')
        user.nationality = request.POST.get('nationality')
        user.phone = request.POST.get('phone')
        if user.role == 'driver':
            user.nid_card_no = request.POST.get('nid_card_no')
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']
        user.save()
        # messages.success(request, 'Profile information saved successfully!')
        return redirect('home')
    return render(request, 'gocart/complete_profile.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.gender = request.POST.get('gender')
        user.dob = request.POST.get('dob')
        user.present_address = request.POST.get('present_address')
        user.postal_code = request.POST.get('postal_code')
        user.home_district = request.POST.get('home_district')
        user.nationality = request.POST.get('nationality')
        user.phone = request.POST.get('phone')
        if user.role == 'driver':
            user.nid_card_no = request.POST.get('nid_card_no')
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']
        user.save()
        return redirect('profile')
    return render(request, 'gocart/profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'gocart/change_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = request.user
        if user.check_password(password):
            user.delete()
            logout(request)
            # messages.success(request, 'Your account has been deleted.')
            return redirect('home')
        else:
            # messages.error(request, 'Incorrect password. Please try again.')
            return redirect('delete_account')  # Stay on the confirmation page
    elif request.method == 'GET':
        return render(request, 'gocart/delete_account.html')
    return HttpResponseForbidden('Invalid method')
