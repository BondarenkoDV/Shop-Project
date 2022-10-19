from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

"""
Модель пользователя взята, для его регистрации, путем передачи значений в формы RegisterUserForm и LoginUserForm
Настроены нужные поля для регистрации и авторизации.
"""


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    first_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    password1 = forms.CharField(label='Пароль', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    password2 = forms.CharField(label='Повтор пароля', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    password = forms.CharField(label='Пароль', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
