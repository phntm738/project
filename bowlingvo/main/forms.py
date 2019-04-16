from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин:',
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин'})
    )
    password = forms.CharField(
        label='Пароль:',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин:',
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин'})
    )
    email = forms.EmailField(
        label='Email:',
        required=True,
        help_text="Введите правильный email.",
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
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


class EditProfileForm(PasswordChangeForm):
    username = forms.CharField(
        label='Сменить имя пользователя:',
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'})
    )
    email = forms.EmailField(
        label='Сменить email (требуется подтверждение):',
        required=False,
        help_text="Введите правильный email.",
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    old_password = forms.CharField(
        label='Введите старый пароль:',
        required=False,
        strip=False,
        help_text='Введите старый пароль.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Старый пароль'}),
    )
    new_password1 = forms.CharField(
        label='Введите новый пароль:',
        required=False,
        strip=False,
        help_text='Введите новый пароль.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'}),
    )
    new_password2 = forms.CharField(
        label='Повторите новый пароль:',
        required=False,
        strip=False,
        help_text='Повторите новый пароль.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите новый пароль'}),
    )
