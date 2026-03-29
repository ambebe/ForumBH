from django.urls import path
from .views import profile_view
from mainpage import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='base'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile')
]