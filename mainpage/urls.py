from django.urls import path
from .views import edit_profile
from mainpage import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='base'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile')
]