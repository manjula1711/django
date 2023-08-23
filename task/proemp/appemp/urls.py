

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('addmembers/', views.addmembers, name='addmembers'),
    path('login/', views.loginpage, name='loginpage'),
    path('check/', views.check, name='check'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

