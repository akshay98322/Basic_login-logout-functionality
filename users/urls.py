from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register-user/', views.registerUser, name='register-user'),
    path('user-home/', views.home, name='user-home'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
