from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from main_page import views

# Create your views here.


class MyLogout(LogoutView):
    next_page = reverse_lazy(views.home)

class AboutMeView(TemplateView):
    template_name = 'shop_auth/about-user.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'shop_auth/register.html'
    success_url = reverse_lazy('myauth:about-user')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response