from django.urls import path
from .views import index, simple_view

urlpatterns = [
    path('', simple_view),
    
]