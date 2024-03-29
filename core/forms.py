from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    widgets = {
        'username': forms.TextInput(
            attrs={'placeholder': 'Your username', 'class': 'w-full py-4 px-6 rounded-xl purple-input'}),
        'password': forms.PasswordInput(
            attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl purple-input'})
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field, widget in self.widgets.items():
            self.fields[field].widget.attrs.update(widget.attrs)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    widgets = {
        'username': forms.TextInput(
            attrs={'placeholder': 'Your username', 'class': 'w-full py-4 px-6 rounded-xl purple-input'}),
        'email': forms.EmailInput(
            attrs={'placeholder': 'Your email address', 'class': 'w-full py-4 px-6 rounded-xl purple-input'}),
        'password1': forms.PasswordInput(
            attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl purple-input'}),
        'password2': forms.PasswordInput(
            attrs={'placeholder': 'Repeat password', 'class': 'w-full py-4 px-6 rounded-xl purple-input'}),
    }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field, widget in self.widgets.items():
            self.fields[field].widget.attrs.update(widget.attrs)
