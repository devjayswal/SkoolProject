from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
from .models import PasswordResetRequest


# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user  = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role=role,
        )

        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True
        
        user.save()
        login(request, user)
        messages.success(request, 'Sign up successfully.')
        return redirect('index')
    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            
            if user.is_student:
                return redirect('dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_admin:
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'User role is not defined.')
                return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'authentication/login.html')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.filter(email=email).first()
            
            if user:
                token = get_random_string(length=32)
                reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
                reset_request.send_reset_email()
                messages.success(request, 'Password reset link has been sent to your email.')
            else:
                messages.success(request, 'email not found')
        except User.DoesNotExist:
            messages.error(request, 'Email not found.')
    return render(request, 'authentication/forget_password.html')

def reset_password_view(request,token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()
    if not reset_request or not reset_request.is_valid():
        messages.error(request, 'Invalid or expired token.')
        return redirect('index')
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request, 'Password has been reset successfully.')
        return redirect('login')
    return render(request, 'authentication/reset-password.html', {'token': token})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('index')