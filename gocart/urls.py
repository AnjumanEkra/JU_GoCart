from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # actual login logic
    path('logout/', views.logout_view, name='logout'),
    path('logout/confirm/', views.confirm_logout, name='confirm_logout'),
]