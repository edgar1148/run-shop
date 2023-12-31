from typing import Any

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()


class UserCreateForm(UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Ваш Email'
        self.fields['email'].required = True
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists() and len(email) > 254:
            raise forms.ValidationError(
                "Email уже зарегистрирован или слишком длинный")

        return email


class LoginForm(AuthenticationForm):
    """Форма аутентификации пользователя."""
    username = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'


class UserUpdateForm(forms.ModelForm):
    """Форма редактирования пользователя."""
    email = forms.EmailField(required=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Ваш Email'
        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(
            email=email).exclude(
                id=self.instance.id).exists() or len(email) > 254:
            raise forms.ValidationError("Email is already in use or too long")
        return email

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ('password1', 'password2')
