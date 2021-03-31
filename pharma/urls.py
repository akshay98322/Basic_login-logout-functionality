from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

]
