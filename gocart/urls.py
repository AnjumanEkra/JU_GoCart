from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # actual login logic
    path('logout/', views.logout_view, name='logout'),
    path('logout/confirm/', views.confirm_logout, name='confirm_logout'),

    # Password Reset Flow
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='gocart/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='gocart/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='gocart/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='gocart/password_reset_complete.html'), name='password_reset_complete'),

    # Profile
    path('complete-profile/', views.complete_profile, name='complete_profile'),
]