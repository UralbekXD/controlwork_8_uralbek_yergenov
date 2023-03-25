from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    avatar = forms.ImageField()
    phone_number =

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'avatar',
            'password1',
            'password2',
            'first_name',
            'last_name',

        ]