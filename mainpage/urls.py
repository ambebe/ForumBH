from django.urls import path
from .views import edit_profile
from mainpage import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='base'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('create-topic/', views.create_post, name='post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]