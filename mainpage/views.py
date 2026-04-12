from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from .forms import LoginForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Item


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('base')  # Після успішного входу переходимо на домашню сторінку

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)
        

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Після успішної реєстрації переходимо на сторінку логіну

def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile.html", {"form": form})

def simple_view(request):
    return render(request, "base.html")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'
