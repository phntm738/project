from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль:', strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин:', required=True, widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email:',
                             required=True,
                             help_text="Enter a valid email.",
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(
                            label='Пароль:',
                            required=True,
                            strip=False,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
    )
    password2 = forms.CharField(
                            label='Повторите пароль:',
                            required=True,
                            strip=False,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
