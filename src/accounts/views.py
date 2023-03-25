from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import SignUpForm


# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
