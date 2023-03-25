from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import SignUpForm


# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
